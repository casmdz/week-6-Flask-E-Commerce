{% extends 'base.html' %}

{% block content %}



# <h1>Update Post # {{ post.id }}</h1>

# <form method="POST" class="container col-4">
#     {{ form.hidden_tag() }}

#     {{ form.title(class='form-control', placeholder='Title', value= post.title) }}
#     {{ form.img_url(class='form-control', placeholder='Image URL', value= post.img_url ) }}
#     {{ form.caption(class='form-control', placeholder='Caption', value= post.caption ) }}
    
#     {{ form.submit(class='btn btn-primary') }}
# </form>



{% endblock %}