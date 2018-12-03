---
title: People
permalink: /people/
---

{% assign people_sorted = (site.people | sort: 'joined' %}
{% assign people_array = "pi|postdoc|gradstudent|visiting|others|alumni" | split: "|" %}

{% for item in people_array %}

<div class="pos_header">
{% if item == 'postdoc' %}
<h3>Postdoctoral Fellows</h3>
 {% elsif item == 'pi' %}
<h3>Principal Investigator</h3>
 {% elsif item == 'gradstudent' %}
<h3>Graduate Students</h3>
 {% elsif item == 'visiting' %}
<h3>Visiting Scholars</h3>
 {% elsif item == 'others' %}
<h3>Honorary Members</h3>
 {% elsif item == 'alumni' %}
<h3>Alumni</h3>
{% endif %}
</div>

<div class="content list people">
  {% for profile in people_sorted %}
    {% if profile.position contains item %}
    <div class="list-item-people">
      <p class="list-post-title">
        {% if profile.avatar %}
        <a href="{{ site.baseurl }}{{ profile.url }}"><img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
        {% else %}
        <a href="{{ site.baseurl }}{{ profile.url }}"><img width="200" src="http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"></a>
        {% endif %}
        <a class="name" href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>    
    {% endif %}
  {% endfor %}
</div>
<hr>
{% endfor %}


| Who are they | When were they here | Where they went |
| :------------- |:-------------| :-----------|
| [Eva Dyer](http://evadyer.github.io/) | Postdoc (2017) | Assistant Professor, Dept of Biomedical Engineering at Georgia Tech and Emory U
| [Pavan Ramkumar](http://kordinglab.com/people/pavan_ramkumar/index.html) | Postdoc (2017) | A secret startup in bay area
| [Pat Lawlor](http://kordinglab.com/people/pat_lawlor/index.html) | Graduate student (2016) | Northwestern Medical school
| [Hugo Fernandes](http://kordinglab.com/people/hugo_fernandes/index.html) | Postdoc (2016) | [rockets of awesome](https://www.rocketsofawesome.com/)
| [Torben Noto](http://kordinglab.com/people/torben_noto/index.html) | Rotation Student (2016) | Northwestern
| [Vivek Sagar](http://kordinglab.com/people/vivek_sagar/index.html) | Rotation Student (2016) | Northwestern
| [David Brandfonbrener](http://kordinglab.com/people/david_brandfonbrener/index.html) | Visiting Scholar (2016)  | PhD Student, Yale university
| [Daniel E. Acuna](http://kordinglab.com/people/daniel_e_acuna/index.html) | Postdoc (2016) | [iSchool at Syracuse](https://ischool.syr.edu/people/directories/view/deacuna/)
| [Cong Yin (Lily)](http://kordinglab.com/people/cong_yin/index.html) | Visiting scholar (2015-2016) | Peking University |


