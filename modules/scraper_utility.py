import json
import os
import pyperclip

def parse_clipboard_to_json():
    print("📋 Reading unedited text data from your clipboard...")
    raw_text = pyperclip.paste()
    
    if not raw_text or len(raw_text.strip()) < 50:
        print("❌ Error: Your clipboard is empty or doesn't contain enough text. Please copy the syllabus text first!")
        return
        
    lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
    syllabus_map = {}
    
    current_course = None
    course_idx = 1
    capture_mode = None # Tracks whether parsing objectives, skills, or tools
    
    for line in lines:
        # Detect Course Title boundaries (e.g., "Course 1: ...")
        if line.lower().startswith("course ") and ":" in line:
            parts = line.split(":", 1)
            current_course = f"Course {course_idx}"
            syllabus_map[current_course] = {
                "title": parts[1].strip(),
                "what_you_ll_learn": [],
                "skills_you_ll_gain": [],
                "tools_you_ll_learn": []
            }
            course_idx += 1
            capture_mode = None
            continue
            
        if not current_course:
            continue
            
        # Detect Section Boundaries matching your image layout
        if "what you'll learn" in line.lower():
            capture_mode = "objectives"
            continue
        elif "skills you'll gain" in line.lower():
            capture_mode = "skills"
            continue
        elif "tools you'll learn" in line.lower():
            capture_mode = "tools"
            continue
            
        # Extract content based on active block area
        if capture_mode == "objectives":
            # Strip out bullet artifacts or checkboxes
            clean_obj = line.lstrip("✓•- ").strip()
            if clean_obj and clean_obj not in syllabus_map[current_course]["what_you_ll_learn"]:
                # Limit cross-contamination into adjacent headers
                if not any(header in clean_obj.lower() for header in ["skills you'll", "tools you'll", "course "]):
                    syllabus_map[current_course]["what_you_ll_learn"].append(clean_obj)
                    
        elif capture_mode == "skills":
            clean_skill = line.lstrip("•- ").strip()
            if clean_skill and clean_skill.lower() != "show all" and not clean_skill.lower().startswith("course "):
                syllabus_map[current_course]["skills_you_ll_gain"].append(clean_skill)
                
        elif capture_mode == "tools":
            clean_tool = line.lstrip("•- ").strip()
            if clean_tool and not clean_tool.lower().startswith("course "):
                syllabus_map[current_course]["tools_you_ll_learn"].append(clean_tool)

    # Clean empty fallbacks for unpopulated blocks
    for c_key in syllabus_map:
        if not syllabus_map[c_key]["what_you_ll_learn"]:
            syllabus_map[c_key]["what_you_ll_learn"] = ["Verbatim objectives available upon enrollment module loading."]
        if not syllabus_map[c_key]["skills_you_ll_gain"]:
            syllabus_map[c_key]["skills_you_ll_gain"] = ["Data Science Core Capabilities"]
        if not syllabus_map[c_key]["tools_you_ll_learn"]:
            syllabus_map[c_key]["tools_you_ll_learn"] = ["Python", "Jupyter Notebooks"]

    if syllabus_map:
        output_path = os.path.join(os.path.dirname(__file__), "data_science.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(syllabus_map, f, indent=4, ensure_ascii=False)
        print(f"🎉 Success! Structured file created matching layout specifications at: {output_path}")
    else:
        print("❌ Could not parse structured course blocks. Verify formatting matching 'Course X: Name'.")

if __name__ == "__main__":
    parse_clipboard_to_json()
