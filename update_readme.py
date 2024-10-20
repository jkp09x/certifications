#!/opt/anaconda3/bin/python3

import os
import re

def camel_case_to_spaces(name):
    return re.sub(r'(?<!^)(?<![A-Z])(?=[A-Z])', ' ', name)

def parse_filename(filename):
    pattern_with_specialization = r'^(?P<site>\w+?)_(?P<specialization>[^_]+?)_(?P<course>.+)\.pdf$'
    pattern_without_specialization = r'^(?P<site>\w+?)_(?P<course>.+)\.pdf$'

    match = re.match(pattern_with_specialization, filename)
    if match:
        return match.group('site'), match.group('specialization'), match.group('course')

    match = re.match(pattern_without_specialization, filename)
    if match:
        return match.group('site'), None, match.group('course')

    return None, None, None

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
                dispSite = camel_case_to_spaces(site)
                dispCourse = camel_case_to_spaces(course)
                # Set specialization to empty string if None
                if specialization is None:
                    dispSpecialization = ''
                else:
                    dispSpecialization = camel_case_to_spaces(specialization)
                path = os.path.join(cert_dir, filename)
                certifications.append((dispSite, dispSpecialization, dispCourse, path))

    readme_content = generate_readme(certifications)

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    update_readme()

