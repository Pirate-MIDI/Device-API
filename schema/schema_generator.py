#!/usr/bin/python3

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

config = GenerationConfiguration(copy_css=False, expand_buttons=True, template_name="md", show_breadcrumbs=True,
											with_footer=False,)

generate_from_filename("schema/device_settings_schema.json", "schema/outputs/device_settings_schema_doc.md", config=config)
generate_from_filename("schema/global_settings_schema.json", "schema/outputs/global_settings_schema.md", config=config)
generate_from_filename("schema/bank_settings_schema.json", "schema/outputs/bank_settings_schema.md", config=config)

config = GenerationConfiguration(expand_buttons=True, template_name="js_offline", show_breadcrumbs=True)

generate_from_filename("schema/device_settings_schema.json", "schema/outputs/device_settings_schema_doc.html", config=config)
generate_from_filename("schema/global_settings_schema.json", "schema/outputs/global_settings_schema.html", config=config)
generate_from_filename("schema/bank_settings_schema.json", "schema/outputs/bank_settings_schema.html", config=config)