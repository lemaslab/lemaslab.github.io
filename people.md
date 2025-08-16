---
title: People
permalink: /people/
---

{% assign sorted_people = site.people | sort: 'joined' %}
{% assign people_array = "pi|researchCoordinator|gradStudent|underGradStudent|alumni" | split: "|" %}

{% for item in people_array %}

<div class="pos_header">
{% if item == 'gradStudent' %}
<h3>Graduate Students</h3>
{% elsif item == 'researchCoordinator' %}
<h3>Research Coordinator</h3>
{% elsif item == 'pi' %}
<h3>Principal Investigator</h3>
{% elsif item == 'underGradStudent' %}
<h3>Undergrad Students</h3>
{% elsif item == 'alumni' %}
<h3>Alumni</h3>
{% endif %}
</div>

<div class="content list people">
  {% for profile in sorted_people %}
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
| Luran Manfio | Undergradaute (2015-2019) | TBD |
| Andrew Schleffer | Undergradaute (2015-2019) | TBD |
| Emily Colgate | Undergradaute (2015-2019) | TBD |
| Joshua Breuwet | Undergradaute (2015-2019) | TBD |
| Lauren Wright | Undergradaute (2015-2019) | Miller School of Medicine, University of Miami |
| Austen Hentschel | Undergradaute (2015-2019) | TBD |
| Lynn Chen | Undergradaute (2015-2019) | TBD |
| Yasmin Garcia | Undergradaute (2015-2019) | TBD |
| Yasmine Gillespie | Undergradaute (2015-2019) | University of Florida College of Medicine |
| Magda Francois | Research Coordinator (2015-2022) | TBD |
| Xinsong Du | Ph.D. student (2017-2023) | Postdoctoral Researcher at Harvard |
| Braeden Lewis | Master student (2019-2020) | TBD |
| Yangru Zhou | Master student (2019-2020) | TBD |
| Samantha DePaul | Undergraduate student (2019-2020) | TBD |
| Hailey Ballard | Undergraduate student (2019-2021) | University of Wisconsin-Madison |
| Sakina Johar | Undergraduate student (2019-2021) | TBD |
| Nisha Chachad | Undergraduate student (2019-2022) | TBD |


