---
title: People
permalink: /people/
---

{% assign people_sorted = (site.people | sort: 'joined' %}
{% assign people_array = "pi|clinical|gradStudent|student" | split: "|" %}

{% for item in people_array %}

<div class="pos_header">
{% if item == 'gradStudent' %}
<h3>Graduate Students</h3>
{% elsif item == 'clinical' %}
<h3>Clinical Team</h3>
{% elsif item == 'pi' %}
<h3>Principal Investigator</h3>
{% elsif item == 'student' %}
<h3>Undergrad Students</h3>
{% endif %}
</div>

<div class="content list people">
  {% for profile in people_sorted %}
    {% if profile.position contains item %}
    <div class="list-item-people">
      <p class="list-post-title">
        {% if profile.avatar %}
        <a href="{{ site.baseurl }}{{ profile.url }}"><img width="200" height="323.6" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
        {% else %}
        <a href="{{ site.baseurl }}{{ profile.url }}"><img width="200" height="323.6" src="http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"></a>
        {% endif %}
        <a class="name" href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>    
    {% endif %}
  {% endfor %}
</div>
<hr>
{% endfor %}


| Who are they  | When were they here | Where they went |
| :-------------- |:-------------| :-----------|
| Luran Manfio | Undergradaute (2015-2018) | TBD |
| Austen Hentschel | Undergradaute (2015-2018) | TBD |
| Lynn | Undergradaute (2015-2018) | TBD |
| Magda Francois | clincal (2015-2018) | TBD |
| Xinsong Du | Ph.D. student (2017-present) | TBD |