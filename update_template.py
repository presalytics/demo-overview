import presalytics

def dummy_api_call_or_sql_query():
    return {"replace_map" : {
        'Account.Name': 'Presalytics.io',
        'Contact1.Name': 'Kevin Hannegan',
        'Contact1.Title': 'Founder',
        'Contact1.Email': 'kevin@presalytics.io',
        'Contact1.Notes': 'This is a test note 1',
        'Contact2.Name': 'John Boet',
        'Contact2.Title': 'Advisor (For now)',
        'Contact2.Email': 'john@presalytics.io',
        'Contact2.Notes': 'This is a test demo'
    }
}
    

outline: presalytics.StoryOutline = presalytics.StoryOutline.import_yaml('story.yaml')

template_widget = outline.pages[2].widgets[0]

text_transform_metadata = dummy_api_call_or_sql_query()

new_widget = presalytics.OoxmlEditorWidget(
    name="New Widget with filed in Text",
    story_id=template_widget.data["story_id"],
    object_ooxml_id=template_widget.data["object_ooxml_id"],
    endpoint_map=presalytics.OoxmlEndpointMap.slide(),
    transform_class=presalytics.TextReplace,
    transform_params=text_transform_metadata
)

outline.pages[2].widgets[0] = new_widget.serialize()

outline.export_yaml('story.yaml')



