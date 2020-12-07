import presalytics # imports the presalytics python package

def dummy_api_call_or_sql_query():
    """
    This method similates an API or data query query to a local database.  This database 
    could reside on a local machine or inside corporate network.

    Every this script is run, the data recieved from the API call or database query could change, and the story
    will be updated accordingly.  This is helpful for creating live updating dashboard and reports.
    """
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
    
# Turn the local copy of story outline, "story.yaml", into a python object
outline: presalytics.StoryOutline = presalytics.StoryOutline.import_yaml('story.yaml')

text_transform_metadata = dummy_api_call_or_sql_query()  # Simulates an API call / database query

# Store the serialized widget that we are going to update in a python variable called "template_widget"
for i in range(0, len(outline.pages)):
        
    template_widget = outline.pages[i].widgets[0]

    # Creates a new widget that dynamically updates the page as the result of dummy_api_call_or_sql_query() change
    new_widget = presalytics.OoxmlEditorWidget(
        name="New Widget with filed in Text",  # A name -- can be any string that describes the widget
        story_id=template_widget.data["story_id"],  # The story Id
        object_ooxml_id=template_widget.data["object_ooxml_id"],  # A reference in the presalytics API to the slide we are updating
        endpoint_map=presalytics.OoxmlEndpointMap.slide(),  # The type of object we are updating (Defines the endpoint for Presalytics API calls)
        transform_class=presalytics.TextReplace,  # The action that we want this widget to take
        transform_params=text_transform_metadata  # The metadata that the action uses to transform the Widget (e.g, from API call)
    )

    outline.pages[i].widgets[0] = new_widget.serialize()  # update the python representation of the story outline

    del template_widget

outline.export_yaml('story.yaml')  # write the outline to the story.yaml file



