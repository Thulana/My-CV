#!/usr/bin/env python3
"""
CV Generator - Creates ATS-friendly HTML resume from YAML data
Usage: python generate_html.py
Output: cv-output.html (can be opened in browser and printed to PDF)
"""

import yaml
from datetime import datetime


def load_cv_data(yaml_file='cv-data.yaml'):
    """Load CV data from YAML file"""
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)


def generate_html(data):
    """Generate ATS-friendly HTML from CV data"""
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['personal']['first_name']} {data['personal']['last_name']} - Resume</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: Arial, Calibri, sans-serif;
            font-size: 10pt;
            line-height: 1.25;
            color: #000;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 0.35in 0.5in;
            background: white;
        }}
        
        /* Print optimization */
        @media print {{
            @page {{
                margin: 0.4in 0.5in;
                size: letter;
            }}
            body {{
                padding: 0.35in 0.5in;
                margin: 0;
            }}
            .no-print {{
                display: none;
            }}
        }}
        
        /* Header */
        .header {{
            text-align: center;
            margin-bottom: 8px;
            border-bottom: 2px solid #000;
            padding-bottom: 4px;
        }}
        
        .name {{
            font-size: 18pt;
            font-weight: bold;
            margin-bottom: 2px;
        }}
        
        .title {{
            font-size: 11pt;
            margin-bottom: 4px;
            color: #333;
        }}
        
        .contact {{
            font-size: 9pt;
            line-height: 1.4;
        }}
        
        .contact a {{
            color: #000;
            text-decoration: none;
        }}
        
        /* Section headers */
        .section {{
            margin-top: 8px;
            margin-bottom: 4px;
        }}
        
        .section-title {{
            font-size: 11pt;
            font-weight: bold;
            text-transform: uppercase;
            border-bottom: 1px solid #000;
            padding-bottom: 1px;
            margin-bottom: 4px;
        }}
        
        /* Summary */
        .summary {{
            margin-bottom: 4px;
            text-align: justify;
        }}
        
        /* Skills */
        .skill-category {{
            margin-bottom: 3px;
        }}
        
        .skill-category strong {{
            display: inline-block;
            min-width: 180px;
        }}
        
        /* Experience */
        .experience-item {{
            margin-bottom: 6px;
        }}
        
        .experience-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 2px;
        }}
        
        .company-role {{
            font-weight: bold;
        }}
        
        .duration {{
            font-style: italic;
        }}
        
        .location {{
            color: #333;
            font-size: 9pt;
            margin-bottom: 2px;
        }}
        
        .achievements {{
            margin-left: 20px;
            margin-top: 1px;
        }}
        
        .achievements li {{
            margin-bottom: 1px;
        }}
        
        .technologies {{
            font-size: 9pt;
            color: #333;
            margin-top: 2px;
            font-style: italic;
        }}
        
        /* Education */
        .education-item {{
            margin-bottom: 4px;
        }}
        
        .degree {{
            font-weight: bold;
        }}
        
        /* Projects */
        .project-item {{
            margin-bottom: 4px;
        }}
        
        .project-header {{
            font-weight: bold;
        }}
        
        .project-link {{
            color: #0066cc;
            text-decoration: none;
        }}
        
        .project-description {{
            margin-top: 2px;
            margin-bottom: 2px;
        }}
        
        /* Certifications */
        .certification-item {{
            margin-bottom: 2px;
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <div class="name">{data['personal']['first_name'].upper()} {data['personal']['last_name'].upper()}</div>
        <div class="title">{data['personal']['tagline']}</div>
        <div class="contact">
            {data['contact']['phone']} | 
            <a href="mailto:{data['contact']['email']}">{data['contact']['email']}</a> | 
            {data['contact']['location']}<br>
            LinkedIn: <a href="https://linkedin.com/in/{data['contact']['linkedin']}">{data['contact']['linkedin']}</a> | 
            GitHub: <a href="https://github.com/{data['contact']['github']}">{data['contact']['github']}</a> | 
            <a href="https://{data['contact']['website']}">{data['contact']['website']}</a>
        </div>
    </div>
    
    <!-- Professional Summary -->
    <div class="section">
        <div class="section-title">Professional Summary</div>
        <div class="summary">{data['summary'].strip()}</div>
    </div>
    
    <!-- Skills -->
    <div class="section">
        <div class="section-title">Skills</div>
"""
    
    # Add skills
    for skill in data['skills']:
        skills_list = ' | '.join(skill['items'])
        html += f"""        <div class="skill-category">
            <strong>{skill['category']}:</strong> {skills_list}
        </div>
"""
    
    html += """    </div>
    
    <!-- Work Experience -->
    <div class="section">
        <div class="section-title">Work Experience</div>
"""
    
    # Add experience
    for exp in data['experience']:
        end_date = exp['end_date'] if exp['end_date'] != 'Present' else 'Present'
        html += f"""        <div class="experience-item">
            <div class="experience-header">
                <div class="company-role">{exp['company']} | {exp['role']}</div>
                <div class="duration">{exp['start_date']} - {end_date}</div>
            </div>
            <div class="location">{exp['location']}</div>
            <ul class="achievements">
"""
        for achievement in exp['achievements']:
            html += f"""                <li>{achievement}</li>
"""
        
        tech_list = ', '.join(exp['technologies'])
        html += f"""            </ul>
            <div class="technologies">Technologies: {tech_list}</div>
        </div>
"""
    
    html += """    </div>
    
    <!-- Education -->
    <div class="section">
        <div class="section-title">Education</div>
"""
    
    # Add education
    for edu in data['education']:
        html += f"""        <div class="education-item">
            <div class="degree">{edu['degree']}</div>
            <div>{edu['institution']}, {edu['location']} | Graduated: {edu['graduation_year']}</div>
"""
        if 'gpa' in edu and edu['gpa']:
            html += f"""            <div>GPA: {edu['gpa']}</div>
"""
        html += """        </div>
"""
    
    html += """    </div>
    
    <!-- Projects -->
    <div class="section">
        <div class="section-title">Projects</div>
"""
    
    # Add projects
    for project in data['projects']:
        project_title = project['name']
        if 'url' in project:
            project_title = f'<a href="{project["url"]}" class="project-link">{project_title}</a>'
        if 'github' in project:
            project_title += f' | <a href="https://github.com/{project["github"]}" class="project-link">GitHub</a>'
            
        html += f"""        <div class="project-item">
            <div class="project-header">{project_title} | {project['duration']}</div>
            <div class="project-description">{project['description']}</div>
            <div class="technologies">Technologies: {', '.join(project['technologies'])}</div>
        </div>
"""
    
    html += """    </div>
    
    <!-- Publications -->"""
    
    if 'publications' in data and data['publications']:
        html += """
    <div class="section">
        <div class="section-title">Publications</div>
"""
        for pub in data['publications']:
            pub_title = pub['title']
            if 'url' in pub:
                pub_title = f'<a href="{pub["url"]}" class="project-link">{pub_title}</a>'
            html += f"""        <div class="certification-item">
            <strong>{pub_title}</strong> | {pub['venue']} | {pub['year']}
        </div>
"""
        html += """    </div>
    """
    
    # Only show certifications if they exist
    if 'certifications' in data and data['certifications']:
        html += """
    <!-- Certifications -->
    <div class="section">
        <div class="section-title">Certifications</div>
"""
        for cert in data['certifications']:
            html += f"""        <div class="certification-item">
            <strong>{cert['name']}</strong> | {cert['issuer']} | {cert['year']}
        </div>
"""
        html += """    </div>
    """
    
    html += """
    <div class="no-print" style="margin-top: 30px; padding: 20px; background: #f0f0f0; border-radius: 5px;">
        <strong>Instructions:</strong>
        <ul style="margin-left: 20px; margin-top: 10px;">
            <li>To save as PDF: Press Ctrl+P (or Cmd+P on Mac) and select "Save as PDF"</li>
            <li>Make sure to set margins to "Minimum" or "None" in print settings</li>
            <li>Ensure "Background graphics" is enabled</li>
        </ul>
    </div>
</body>
</html>
"""
    
    return html


def main():
    """Main function"""
    print("Loading CV data from cv-data.yaml...")
    data = load_cv_data()
    
    print("Generating ATS-friendly HTML...")
    html = generate_html(data)
    
    output_file = 'cv-output.html'
    with open(output_file, 'w') as f:
        f.write(html)
    
    print(f"✓ Successfully generated {output_file}")
    print(f"  Open it in your browser and print to PDF (Ctrl+P / Cmd+P)")
    print(f"  The PDF will be ATS-friendly and ready for job applications!")


if __name__ == '__main__':
    main()
