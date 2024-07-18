def generate_invitations(template, attendees):
    import os

    # Verifica tipos de entrada
    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: The assistants should be a list of dictionaries")
        return

    # Maneja plantilla vacía
    if not template.strip():
        print("Error: The template is empty, no output files were generated.")
        return

    # Maneja lista vacía de asistentes
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Procesar cada asistente y generar archivos de salida
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for key, value in attendee.items():
            placeholder = "{" + key + "}"
            output_content = output_content.replace(placeholder, value if value else "N/A")

        # Reemplazar cualquier placeholder que se no sea encontrado
        output_content = output_content.format(name="N/A", event_title="N/A", event_date="N/A", event_location="N/A")

        # Escribir archivo de salida
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
