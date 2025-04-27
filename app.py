import openai
from fpdf import FPDF
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this in your environment

# Collect user information
def collect_user_info():
    print("Please enter your details for resume generation:")
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    education = input("Education Details: ")
    experience = input("Work Experience: ")
    skills = input("Skills (comma separated): ")
    return name, email, phone, education, experience, skills

# Generate resume using OpenAI
def generate_resume(name, email, phone, education, experience, skills):
    prompt = f"""
    Create a professional resume for the following information:
    Name: {name}
    Email: {email}
    Phone: {phone}
    Education: {education}
    Experience: {experience}
    Skills: {skills}
    Keep the tone professional, clear, and achievement-focused.
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=800
    )
    return response.choices[0].text.strip()

# Save resume as PDF
def save_to_pdf(content, filename="resume.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)
    
    pdf.output(filename)
    print(f"Resume saved successfully as {filename}")

# Main flow
def main():
    name, email, phone, education, experience, skills = collect_user_info()
    resume_content = generate_resume(name, email, phone, education, experience, skills)
    save_to_pdf(resume_content)

if __name__ == "__main__":
    main()
