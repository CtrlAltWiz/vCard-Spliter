import os

def split_vcf_file(vcf_path, output_folder):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the entire VCF file
    with open(vcf_path, 'r', encoding='utf-8') as vcf_file:
        vcf_content = vcf_file.read()

    # Split the VCF content into individual contacts
    contacts = vcf_content.split('END:VCARD')

    # Save each contact into a separate .vcf file
    for i, contact in enumerate(contacts):
        if contact.strip():  # Avoid empty contacts
            contact = contact + 'END:VCARD\n'  # Add END:VCARD back to each contact
            contact_filename = f'contact_{i + 1}.vcf'
            contact_path = os.path.join(output_folder, contact_filename)
            with open(contact_path, 'w', encoding='utf-8') as contact_file:
                contact_file.write(contact)
            print(f'Saved: {contact_path}')

# Ask the user for the VCF file location
vcf_path = input("Enter the full path to the .vcf file: ")

# Set the output folder in the C: drive
output_folder = 'C:\\Split_VCF_Contacts'

# Call the function to split the VCF file
split_vcf_file(vcf_path, output_folder)

print(f'All contacts have been split and saved in {output_folder}')
