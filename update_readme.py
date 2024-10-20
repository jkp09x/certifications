#!/opt/anaconda3/bin/python3

import os
import re

# TODO: define and process files for different naming conventions
#       1. Coursera_SpecializationName_CourseName✅
#       2. Udacity_Nanodegree_Course
#       3. Udacity_Course
#           a. Coursera_CourseName
#           b. Udacity_CourseName
#           c. Udemy_CourseName
def parse_Coursera_Specialization(filename):
    pattern = r'^(?P<site>\w+)(_(?P<specialization>[^_]+))?_(?P<course>.+)\.pdf$'
    match = re.match(pattern, filename)
    if match:
        return match.group('site'), match.group('specialization'), match.group('course')
    return None, None, None

def parse_Udacity_Nanodegree_Course():
    return

def parse_Coursera_course():
    return

def parse_Udacity_course():
    return

def parse_Udemy_course():
    return

def parse_filename(filename):
    return parse_Coursera_Specialization(filename)

def generate_readme(certifications):
    readme_content = "# Certifications\n\n"
    readme_content += " | Site | Degree Type | Course |\n"
    readme_content += " | -----|-------------|--------|\n"

    for cert in sorted(certifications):
        site, specialization, course, path = cert
        course_link = f"[{course}]({path})"
        readme_content += f"| {site} |  {specialization if specialization else ''} | {course_link} |\n"

    return readme_content

def update_readme():
    certifications = []
    cert_dir = 'certifications'

    for filename in os.listdir(cert_dir):
        if filename.endswith('.pdf'):
            site, specialization, course = parse_filename(filename)
            if site and course:
                path = os.path.join(cert_dir, filename)
                certifications.append((site, specialization, course, path))

    readme_content = generate_readme(certifications)

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    update_readme()

