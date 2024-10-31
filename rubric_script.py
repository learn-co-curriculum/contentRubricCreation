import requests
import csv

# Canvas API configuration
API_URL = "https://flatironlearn.instructure.com:443/api/v1"

def read_rubric_from_csv(file_path):
    rubric_data = {}
    with open(file_path, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        
        # Read the first row (Point Value row)
        points_row = next(reader)[1:]
        
        # Read the second row (Rating Level row)
        rating_levels_row = next(reader)[1:]
        
        # Read the subsequent rows (Criteria)
        for row in reader:
            criterion = row[0]
            descriptions = row[1:]

            rubric_data[criterion] = {
                "points": int(points_row[-1]),  # Assume max point value is the last in the list for the criterion
                "ratings": []
            }

            # Create each rating from the points and descriptions
            for points, rating_level, description in zip(points_row, rating_levels_row, descriptions):
                rating = {
                    "description": rating_level,
                    "long_description": description,
                    "points": int(points)
                }
                rubric_data[criterion]["ratings"].append(rating)

    return rubric_data

def create_rubric(course_id, rubric_title, rubric_data):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    total_points = sum([data["points"] for data in rubric_data.values()])

    rubric = {
        "rubric[title]": rubric_title,
        "rubric[points_possible]": total_points,
        "rubric_association[association_type]": "Course",
        "rubric_association[association_id]": course_id,
        "rubric_association[use_for_grading]": "0",
        "rubric_association[hide_score_total]": "0",
        "rubric_association[hide_points]": "0",
        "rubric_association[hide_outcome_results]": "0",
        "rubric_association[purpose]": "bookmark",
        "rubric[free_form_criterion_comments]": "0",
        "skip_updating_points_possible": "false",
        "rubric_id": "new",
        "title": rubric_title,
        "points_possible": total_points,
        "_method": "POST",
        "rubric[criteria]": []
    }

    # Build each criterion with detailed rating structure
    for i, (criterion, data) in enumerate(rubric_data.items()):
        criterion_data = {
            f"rubric[criteria][{i}][description]": criterion,
            f"rubric[criteria][{i}][long_description]": data.get("long_description", ""),
            f"rubric[criteria][{i}][points]": data["points"],
            f"rubric[criteria][{i}][criterion_use_range]": "false",
            f"rubric[criteria][{i}][id]": f"_{i * 100}"
        }

        # Add each rating for this criterion
        for j, rating in enumerate(data["ratings"]):
            criterion_data.update({
                f"rubric[criteria][{i}][ratings][{j}][description]": rating["description"],
                f"rubric[criteria][{i}][ratings][{j}][long_description]": rating.get("long_description", ""),
                f"rubric[criteria][{i}][ratings][{j}][points]": rating["points"],
                f"rubric[criteria][{i}][ratings][{j}][id]": f"rating_{i}_{j}"
            })

        rubric.update(criterion_data)

    # Create the rubric with populated criteria and ratings
    response = requests.post(f"{API_URL}/courses/{course_id}/rubrics", headers=headers, data=rubric)

    if response.status_code in [200, 201]:
        try:
            rubric_id = response.json().get('rubric', {}).get('id', None)
            print("Rubric created successfully.")
            if rubric_id:
                associate_rubric_with_course(course_id, rubric_id)
        except KeyError:
            print("Failed to retrieve rubric ID. Full response:", response.json())
    else:
        print(f"Failed to create rubric: {response.status_code}, {response.text}")


def associate_rubric_with_course(course_id, rubric_id):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    data = {
        "rubric_association[rubric_id]": rubric_id,
        "rubric_association[association_type]": "Course",
        "rubric_association[use_for_grading]": "true"
    }

    response = requests.post(f"{API_URL}/courses/{course_id}/rubric_associations", headers=headers, data=data)

    if response.status_code in [200, 201, 500]:
        print("Rubric associated with course successfully.")
    else:
        print(f"Failed to associate rubric with course: {response.status_code}, {response.text}")


# Usage
csv_file_path = "Untitled spreadsheet - Sheet1.csv"
course_id = input("Enter the Canvas course ID: ")
rubric_title = input("Enter the title for the rubric: ")
API_TOKEN = input("Enter your_canvas_api_token: ")

rubric_data = read_rubric_from_csv(csv_file_path)
create_rubric(course_id, rubric_title, rubric_data)
