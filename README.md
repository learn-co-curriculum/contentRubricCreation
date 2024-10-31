# Canvas Rubric Automation Tool 

This project enables instructional designers to automate the creation and association of rubrics in Canvas LMS using Python. Rubric data can be read from a CSV file, parsed, and then used to generate and associate a rubric with a specified Canvas course. 

## Requirements

- Python 3.x installed on your system
- Git for cloning the repository
- API token from Canvas (required to create and associate rubrics programmatically)
- Canvas course ID where the rubric will be created

## Setup Instructions 

### Step 1: Create a Local Directory and Clone the Repository (only done the very first time)
1. Create a directory on your local machine to store the project files: 
```bash
mkdir rubric_automation
cd rubric_automation
```
2. Clone the repository from GitHub:
```bash
git clone https://github.com/learn-co-curriculum/contentRubricCreation.git
cd contentRubricCreation
```
3. Save the CSV file with the rubric data in this project folder and make sure it is named `Untitled spreadsheet - Sheet1.csv`

### Step 2: Configure Canvas API Token 

Your Canvas API token will be used to authenticate with Canvas. You can store it securely and pass it as needed when running the script. 
1. **Retrieve your Canvas API Token**:
   - Go to your Canvas profile settings and scroll to the "Approved Integrations" section.
   - Click "+ New Access Token," give it a name, and copy the generated API token.    
2. **Canvas Course ID**:
   - Find the course ID in your Canvas course URL, which is needed to specify where the rubric should be created.

### Step 3: Run the Script 
Run the main script to generate and associate a rubric based on the CSV data. 
```bash
python3 activate.py
```
The script will prompt you to: 
- Enter your Canvas course ID.
- Give the rubric a title.
- Enter your Canvas API token.

### CSV Format for Rubric Data 
Ensure your CSV file follows the format below for successful parsing: 
| Point Value | 0 | 2 | 4 | 5 | 
|-------------|----|----|----|----| 
| Rating | No Attempt | Attempted | Met Expectations | Excelled | 
| Criterion 1 | Criterion 1 description for each rating | ... | 
| Criterion 2 | Criterion 2 description for each rating | ... | 

### Step 4: Verify in Canvas 
Once the script completes, you should see the rubric on the Canvas course rubrics page under `https://https://flatironlearn.instructure.com/courses/[course_id]/rubrics`. 
## Troubleshooting 
### Permission Denied 
If you encounter a `Permission Denied` error, ensure that you have the necessary execution permissions: 
```bash 
chmod +x rubric_script.py
``` 
### API Errors 
If you encounter an API error, verify your API token and ensure it has the correct permissions. Check the Canvas API documentation or contact Canvas support if needed. 
## Contributing 
Contributions are welcome! Fork the repository and submit a pull request with detailed information about any new features or fixes. 
## License 
This project is licensed under the MIT License. See the `LICENSE` file for details.
