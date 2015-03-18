def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
  <div class="concept-title">
  ''' + "  " + concept_title     
    html_text_2 = '''
  </div>
  <div class="concept-description">
    <p>
  ''' + "    " + concept_description + '''
    </p>'''
    html_text_3 = '''
  </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text 


def write_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description) 

def write_HTML_for_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = write_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

EXAMPLE_LIST_OF_CONCEPTS = [['What does a return statement do', 'Once defined, the function can perform the intended work unless modified. This saves a great deal of time and efforts on the part of programmers'],
                            ]

print write_HTML_for_concepts(EXAMPLE_LIST_OF_CONCEPTS)
        
