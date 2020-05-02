Title: De django à starlette
Date: 2019-05-02 22:00
Author: foxmask
Tags: Django, Starlette
Category: Techno
Slug: de-django-a-starlette
Status: published

<h1>Flashback</h1>
<p>fin 2012, je créais un petit projet et en mai 2013, je sortais une version de ce dernier, nommé "<a href="https://foxmask.net/post/2013/05/27/django-trigger-happy/">Trigger Happy</a>",  entierement conçu avec l'excellentissime framework web <a href="https://www.djangoproject.com/">Django</a>.</p>
<p>7 ans plus tard, <em>en l'écrivant je m'étouffe en réalisant</em>, le projet n'est pas mort mais mais mais depuis l'arrivée d'asyncio, je me suis demandé comment lui apporter un seconde souflle funky, en terme de techno.
Django-Channel vit le jour et promettait de l'async partout mais l'archi me paraissait beaucoup beaucoup trop lourde, en témoigne la palanquée de pré-requis.</p>
<h1>Avant hier</h1>
<p>Lors de l'hacktoberfest 2018 dernier, j'aperçu le projet <a href="https://github.com/kennethreitz/responder">Responder</a>, tout asynchrone, et sortie vitesse lumière à la fin du mois d'octobre, avec moult talentueux contributeurs, dont Tom Christie, "Mr Dango Rest Framework".
Le projet m'attira très fortement, mais encore un petit quelque chose m'empecha de me l'approprier et je laissais alors tomber, avec la flemme et envie d'autre chose.</p>
<h1>Aujourd'hui</h1>
<p>Mais depuis quelques mois, en décortiquant d'avantage les prerequis un à un de responder, je me suis arrêté sur <a href="https://www.starlette.io">starlette</a> (<strong>The little ASGI framework that shines</strong>)
L'auteur de Starlette n'est autre que Tom Christie ;) 
Comme d'hab pour s'approprier le projet, rien de mieux qu'un tuto. </p>
<p>Je tombe alors donc sur <a href="https://github.com/encode/starlette-example/">https://github.com/encode/starlette-example/</a> et hop c'était parti.</p>
<p>Le principe de starlette, pour qui ne connait pas encore le projet, est d'éviter la moindre friction entre les couches que sont la vue, la base de données, les formulaires, etc.</p>
<p>Du coup Starlette propose un socle de base très efficace, et l'auteur de starlette s'est, dans la foulée attelé, à produire des projets péripheriques tels que </p>
<ul>
<li><a href="https://github.com/encode/orm">orm</a> ; pour comme avec Django ; permettre d'utiliser vos tables avec juste Models.object.all()</li>
<li><a href="https://github.com/encode/typesystem">typeschema</a> ; pour la validation de vos formulaires </li>
<li><a href="https://github.com/encode/databases">database</a> ; pour l'abstraction aux SGBD</li>
</ul>
<p>Évidemment tous sont async.</p>
<p>Si vous souhaitez voir une video qui detaille Starlette, Tom Christie donne un talk, commencez donc la vidéo à partir de 7h30 vous aurez une heure à vous régaler ;)</p>
<iframe width="600" height="320" src="https://www.youtube.com/embed/oAV73PRRWNY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<h2>Comme un poisson dans l'eau</h2>
<p>Passer de Django "synchrone" à starlette "asynchrone" devrait être un jeu d'enfant pour vous autres, utilisateurs de Django, comme la plupart des éléments dans starlette, devraient furieusement, vous rappeler des strates de Django.</p>
<h3>Comparatif des couches entre les 2 projets</h3>
<table class="table table-hover table-bordered table-striped">
<tr><th>Périmètre</th><th>Django</th><th>Starlette</th></tr>
<tr><td>Templating</td><td>Template Django</td><td>Jinja2</td></tr>
<tr><td>Vue</td><td>*View</td><td>fonctions dans le(s) module(s) de votre application</td></tr>
<tr><td>Formulaire</td><td> *Form</td><td> typesystem (*)</td>
<tr><td>ORM</td><td>Django ORM</td><td>ORM (*)</td></tr>
<tr><td>"Migration"</td><td>manage.py migrate</td><td>utilisation d'SQL Alchemy</td></tr>
<tr><td>Routage</td><td>urls.py</td><td>Route()</td></tr>
</table>

<p><em><code>(*)</code> = Fonctionnalités non incluses dans starlette, application tierce.</em></p>
<h3>Les projets jumeaux</h3>
<p>Pour vous illustrer le propos, revenons à Trigger Happy.</p>
<p>Alors non je ne l'ai pas refait intégralement avec starlette, mais j'en ai pris 2 morceaux pour produire un petit projet: </p>
<ul>
<li>le premier : l'extraction des flux RSS </li>
<li>le second : l'éditeur markdown nommé <a href="https://joplinapp.org">Joplin</a></li>
</ul>
<p>avec ces 2 là, je créé des notes automatiquement dans Joplin à partir du flux RSS de mon choix</p>
<p>Mon but étant, au départ, de faire la veille techno en créant des notes dans joplin pour les lire ultérieurement à partir de flux RSS de mes sites favoris.</p>
<p>Le premier projet en Django est nommé <a href="https://github.com/foxmask/jong">JONG</a> : <strong>JO</strong>plin <strong>N</strong>ote <strong>G</strong>enerator</p>
<p>Le second projet avec Starlette est nommé <a href="https://github.com/foxmask/yeoboseyo">Yeoboseyo</a></p>
<p>C'est au pif que je me suis mis à recorder Jong à la sauce Starlette, c'est au 3/4 de la fin que je me suis dit</p>
<blockquote>
<p>ho marrant j'ai refait Jong avec Starlette finallement</p>
</blockquote>
<p>et finallement ce n'etait pas la mer à boire, loin s'en faut, et puis c'est modulaire souple et c'est tout ce qu'on attend ;)</p>
<h3>Comment fait on ...</h3>
<p>suis ci dessous, chaque élément du tableau, une fois pour django une fois pour starlette</p>
<h4>... une Vue</h4>
<p>enfin ici il m'aura fallu 3 CBV 
* Django</p>
<div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">RssListView</span><span class="p">(</span><span class="n">ListView</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        list of Rss</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">context_object_name</span> <span class="o">=</span> <span class="s2">&quot;rss_list&quot;</span>
    <span class="n">queryset</span> <span class="o">=</span> <span class="n">Rss</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_queryset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">queryset</span><span class="o">.</span><span class="n">filter</span><span class="p">()</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">&#39;-date_triggered&#39;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_context_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queryset</span><span class="o">.</span><span class="n">filter</span><span class="p">()</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="s1">&#39;-date_triggered&#39;</span><span class="p">)</span>
        <span class="c1"># paginator vars</span>
        <span class="n">record_per_page</span> <span class="o">=</span> <span class="mi">10</span>
        <span class="n">page</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">GET</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;page&#39;</span><span class="p">)</span>
        <span class="c1"># paginator call</span>
        <span class="n">paginator</span> <span class="o">=</span> <span class="n">Paginator</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">record_per_page</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">paginator</span><span class="o">.</span><span class="n">page</span><span class="p">(</span><span class="n">page</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">PageNotAnInteger</span><span class="p">:</span>
            <span class="c1"># If page is not an integer, deliver first page.</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">paginator</span><span class="o">.</span><span class="n">page</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">EmptyPage</span><span class="p">:</span>
            <span class="c1"># If page is out of range (e.g. 9999),</span>
            <span class="c1"># deliver last page of results.</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">paginator</span><span class="o">.</span><span class="n">page</span><span class="p">(</span><span class="n">paginator</span><span class="o">.</span><span class="n">num_pages</span><span class="p">)</span>

        <span class="n">context</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">RssListView</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">get_context_data</span><span class="p">(</span><span class="o">**</span><span class="n">kw</span><span class="p">)</span>
        <span class="n">context</span><span class="p">[</span><span class="s1">&#39;data&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span>
        <span class="k">return</span> <span class="n">context</span>


<span class="k">class</span> <span class="nc">RssCreateView</span><span class="p">(</span><span class="n">RssMixin</span><span class="p">,</span> <span class="n">CreateView</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        list of Rss</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">template_name</span> <span class="o">=</span> <span class="s1">&#39;jong/rss.html&#39;</span>

    <span class="k">def</span> <span class="nf">get_context_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
        <span class="n">context</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">RssCreateView</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">get_context_data</span><span class="p">(</span><span class="o">**</span><span class="n">kw</span><span class="p">)</span>
        <span class="n">context</span><span class="p">[</span><span class="s1">&#39;mode&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;add&#39;</span>
        <span class="k">return</span> <span class="n">context</span>


<span class="k">class</span> <span class="nc">RssUpdateView</span><span class="p">(</span><span class="n">RssMixin</span><span class="p">,</span> <span class="n">UpdateView</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Form to update description</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">template_name</span> <span class="o">=</span> <span class="s1">&#39;jong/rss.html&#39;</span>

    <span class="k">def</span> <span class="nf">get_context_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
        <span class="n">context</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">RssUpdateView</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">get_context_data</span><span class="p">(</span><span class="o">**</span><span class="n">kw</span><span class="p">)</span>
        <span class="n">context</span><span class="p">[</span><span class="s1">&#39;mode&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;Edit&#39;</span>
        <span class="k">return</span> <span class="n">context</span>
</pre></div>


<ul>
<li>Starlette </li>
</ul>
<p>avec Starlette, pas de ClassBasedView :P 
on a une class HTTPEndPoint si on veut mais là pour la petitesse du projet je m'en suis affranchi</p>
<div class="highlight"><pre><span></span><span class="n">async</span> <span class="k">def</span> <span class="nf">homepage</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    get the list of triggers</span>
<span class="sd">    :param request:</span>
<span class="sd">    :return:</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">triggers</span> <span class="o">=</span> <span class="n">await</span> <span class="n">Trigger</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="n">template</span> <span class="o">=</span> <span class="s2">&quot;index.html&quot;</span>
    <span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">&#39;GET&#39;</span><span class="p">:</span>
        <span class="c1"># trigger_id provided, form to edit this one</span>
        <span class="k">if</span> <span class="s1">&#39;trigger_id&#39;</span> <span class="ow">in</span> <span class="n">request</span><span class="o">.</span><span class="n">path_params</span><span class="p">:</span>
            <span class="n">trigger_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">path_params</span><span class="p">[</span><span class="s1">&#39;trigger_id&#39;</span><span class="p">]</span>
            <span class="n">trigger</span> <span class="o">=</span> <span class="n">await</span> <span class="n">Trigger</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">trigger_id</span><span class="p">)</span>
            <span class="n">form</span> <span class="o">=</span> <span class="n">forms</span><span class="o">.</span><span class="n">Form</span><span class="p">(</span><span class="n">TriggerSchema</span><span class="p">,</span> <span class="n">values</span><span class="o">=</span><span class="n">trigger</span><span class="p">)</span>
        <span class="c1"># empty form</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">trigger_id</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="n">form</span> <span class="o">=</span> <span class="n">forms</span><span class="o">.</span><span class="n">Form</span><span class="p">(</span><span class="n">TriggerSchema</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">trigger</span> <span class="ow">in</span> <span class="n">triggers</span><span class="p">:</span>
            <span class="k">print</span><span class="p">(</span><span class="n">trigger</span><span class="p">)</span>
        <span class="n">context</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;request&quot;</span><span class="p">:</span> <span class="n">request</span><span class="p">,</span> <span class="s2">&quot;form&quot;</span><span class="p">:</span> <span class="n">form</span><span class="p">,</span> <span class="s2">&quot;triggers_list&quot;</span><span class="p">:</span> <span class="n">triggers</span><span class="p">,</span> <span class="s2">&quot;trigger_id&quot;</span><span class="p">:</span> <span class="n">trigger_id</span><span class="p">}</span>
        <span class="k">return</span> <span class="n">templates</span><span class="o">.</span><span class="n">TemplateResponse</span><span class="p">(</span><span class="n">template</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>
    <span class="c1"># POST</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">await</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">()</span>
        <span class="n">trigger</span><span class="p">,</span> <span class="n">errors</span> <span class="o">=</span> <span class="n">TriggerSchema</span><span class="o">.</span><span class="n">validate_or_error</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">errors</span><span class="p">:</span>
            <span class="n">form</span> <span class="o">=</span> <span class="n">forms</span><span class="o">.</span><span class="n">Form</span><span class="p">(</span><span class="n">TriggerSchema</span><span class="p">,</span> <span class="n">values</span><span class="o">=</span><span class="n">data</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">)</span>
            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;request&quot;</span><span class="p">:</span> <span class="n">request</span><span class="p">,</span> <span class="s2">&quot;form&quot;</span><span class="p">:</span> <span class="n">form</span><span class="p">,</span> <span class="s2">&quot;triggers_list&quot;</span><span class="p">:</span> <span class="n">triggers</span><span class="p">}</span>
            <span class="k">return</span> <span class="n">templates</span><span class="o">.</span><span class="n">TemplateResponse</span><span class="p">(</span><span class="n">template</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>

        <span class="k">if</span> <span class="s1">&#39;trigger_id&#39;</span> <span class="ow">in</span> <span class="n">request</span><span class="o">.</span><span class="n">path_params</span><span class="p">:</span>
            <span class="n">trigger_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">path_params</span><span class="p">[</span><span class="s1">&#39;trigger_id&#39;</span><span class="p">]</span>
            <span class="n">trigger_to_update</span> <span class="o">=</span> <span class="n">await</span> <span class="n">Trigger</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">trigger_id</span><span class="p">)</span>
            <span class="k">print</span><span class="p">(</span><span class="n">trigger</span><span class="o">.</span><span class="n">rss_url</span><span class="p">,</span> <span class="n">trigger</span><span class="o">.</span><span class="n">joplin_folder</span><span class="p">,</span> <span class="n">trigger</span><span class="o">.</span><span class="n">description</span><span class="p">)</span>
            <span class="n">await</span> <span class="n">trigger_to_update</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">rss_url</span><span class="o">=</span><span class="n">trigger</span><span class="o">.</span><span class="n">rss_url</span><span class="p">,</span>
                                           <span class="n">joplin_folder</span><span class="o">=</span><span class="n">trigger</span><span class="o">.</span><span class="n">joplin_folder</span><span class="p">,</span>
                                           <span class="n">status</span><span class="o">=</span><span class="nb">bool</span><span class="p">(</span><span class="n">trigger</span><span class="o">.</span><span class="n">status</span><span class="p">),</span>
                                           <span class="n">description</span><span class="o">=</span><span class="n">trigger</span><span class="o">.</span><span class="n">description</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">await</span> <span class="n">Trigger</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">rss_url</span><span class="o">=</span><span class="n">trigger</span><span class="o">.</span><span class="n">rss_url</span><span class="p">,</span>
                                         <span class="n">joplin_folder</span><span class="o">=</span><span class="n">trigger</span><span class="o">.</span><span class="n">joplin_folder</span><span class="p">,</span>
                                         <span class="n">description</span><span class="o">=</span><span class="n">trigger</span><span class="o">.</span><span class="n">description</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">RedirectResponse</span><span class="p">(</span><span class="n">request</span><span class="o">.</span><span class="n">url_for</span><span class="p">(</span><span class="s2">&quot;homepage&quot;</span><span class="p">))</span>
</pre></div>


<p>voilà qui remplace les 3 CBV :P</p>
<h4>... un Template</h4>
<ul>
<li>Django</li>
</ul>
<div class="highlight"><pre><span></span><span class="p">&lt;</span><span class="nt">table</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;table table-striped table-hover&quot;</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">tr</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">th</span><span class="p">&gt;</span>{% trans &quot;Name&quot; %}<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">th</span><span class="p">&gt;</span>{% trans &quot;URL&quot; %}<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">th</span><span class="p">&gt;</span>{% trans &quot;Triggered&quot; %}<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">th</span><span class="p">&gt;</span>{% trans &quot;Notebook&quot; %}<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">th</span><span class="p">&gt;</span>{% trans &quot;Bypass Errors&quot; %}<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">th</span><span class="p">&gt;</span>{% trans &quot;Actions&quot; %}<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">tr</span><span class="p">&gt;</span>
{% for data in rss_list %}
<span class="p">&lt;</span><span class="nt">tr</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{% url &#39;edit&#39; data.id %}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;Edit this feed&quot;</span><span class="p">&gt;</span>{{ data.name }}<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{{ data.url }}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;Go to this feed&quot;</span><span class="p">&gt;</span>{{ data.url }}<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{{ data.date_triggered }}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{{ data.notebook }}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{% if data.bypass_bozo %}<span class="p">&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;label label-danger&quot;</span><span class="p">&gt;</span>{% trans &quot;Yes&quot; %}<span class="p">&lt;/</span><span class="nt">span</span><span class="p">&gt;</span>{% else %}<span class="p">&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;label label-success&quot;</span><span class="p">&gt;</span>{% trans &quot;No&quot; %}<span class="p">&lt;/</span><span class="nt">span</span><span class="p">&gt;</span>{% endif %}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-sm btn-md btn-lg btn-success&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;button&quot;</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{% url &#39;edit&#39; data.id %}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;Edit this feed&quot;</span><span class="p">&gt;&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;glyphicon glyphicon-pencil icon-white&quot;</span><span class="p">&gt;&lt;/</span><span class="nt">span</span><span class="p">&gt;&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
        {% if data.status %}
        <span class="p">&lt;</span><span class="nt">a</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-sm btn-md btn-lg btn-primary&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;button&quot;</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{% url &#39;switch&#39; data.id %}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;{% trans &#39;Set this Feed off&#39; %}&quot;</span><span class="p">&gt;&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;glyphicon glyphicon-off icon-white&quot;</span><span class="p">&gt;&lt;/</span><span class="nt">span</span><span class="p">&gt;&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
        {% else %}
        <span class="p">&lt;</span><span class="nt">a</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-sm btn-md btn-lg btn-warning&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;button&quot;</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{% url &#39;switch&#39; data.id %}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;{% trans &#39;Set this Feed on&#39; %}&quot;</span><span class="p">&gt;&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;glyphicon glyphicon-off icon-white&quot;</span><span class="p">&gt;&lt;/</span><span class="nt">span</span><span class="p">&gt;&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
        {% endif %}
        <span class="p">&lt;</span><span class="nt">a</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-sm btn-md btn-lg btn-danger&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;button&quot;</span>  <span class="na">href</span><span class="o">=</span><span class="s">&quot;{% url &#39;delete&#39; data.id %}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;Delete this feed&quot;</span><span class="p">&gt;&lt;</span><span class="nt">span</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;glyphicon glyphicon-trash icon-white&quot;</span><span class="p">&gt;&lt;/</span><span class="nt">span</span><span class="p">&gt;&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
    <span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">tr</span><span class="p">&gt;</span>
{% endfor %}
<span class="p">&lt;/</span><span class="nt">table</span><span class="p">&gt;</span>
</pre></div>


<ul>
<li>Starlette </li>
</ul>
<div class="highlight"><pre><span></span>{% extends &quot;base.html&quot; %}

{% block content %}
<span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;col-xs-5 col-md-5 col-lg-5&quot;</span><span class="p">&gt;</span>
    {% if trigger_id &gt; 0 %}
    <span class="p">&lt;</span><span class="nt">form</span> <span class="na">method</span><span class="o">=</span><span class="s">&quot;POST&quot;</span> <span class="na">action</span><span class="o">=</span><span class="s">&#39;{{ url_for(&#39;</span><span class="na">homepage</span><span class="err">&#39;,</span> <span class="na">trigger_id</span><span class="o">=</span><span class="s">trigger_id)</span> <span class="err">}}&#39;</span><span class="p">&gt;</span>
    {% else %}
    <span class="p">&lt;</span><span class="nt">form</span> <span class="na">method</span><span class="o">=</span><span class="s">&quot;POST&quot;</span> <span class="na">action</span><span class="o">=</span><span class="s">&#39;{{ url_for(&#39;</span><span class="na">homepage</span><span class="err">&#39;)</span> <span class="err">}}&#39;</span><span class="p">&gt;</span>
    {% endif %}
        {{ form }}
        <span class="p">&lt;</span><span class="nt">button</span> <span class="na">type</span><span class="o">=</span><span class="s">&quot;submit&quot;</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-primary&quot;</span><span class="p">&gt;</span>Submit<span class="p">&lt;/</span><span class="nt">button</span><span class="p">&gt;</span>
    <span class="p">&lt;/</span><span class="nt">form</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;col-xs-7 col-md-7 col-lg-7&quot;</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">table</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;table table-striped table-hover&quot;</span><span class="p">&gt;</span>
        <span class="p">&lt;</span><span class="nt">thead</span><span class="p">&gt;</span>
            <span class="p">&lt;</span><span class="nt">tr</span><span class="p">&gt;&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>Description<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>RSS URL<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>Joplin Folder<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>Triggered<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>Created<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>Status<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">th</span> <span class="na">scope</span><span class="o">=</span><span class="s">&quot;col&quot;</span><span class="p">&gt;</span>Action<span class="p">&lt;/</span><span class="nt">th</span><span class="p">&gt;</span>
            <span class="p">&lt;/</span><span class="nt">tr</span><span class="p">&gt;</span>
        <span class="p">&lt;/</span><span class="nt">thead</span><span class="p">&gt;</span>
        {% if triggers_list %}
        <span class="p">&lt;</span><span class="nt">tbody</span><span class="p">&gt;</span>
        {% for trigger in triggers_list %}
            <span class="p">&lt;</span><span class="nt">tr</span><span class="p">&gt;&lt;</span><span class="nt">td</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{{ url_for(&#39;homepage&#39;, trigger_id=trigger.id)}}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;Edit this trigger&quot;</span><span class="p">&gt;</span>{{ trigger.description }}<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{{ trigger.rss_url }}&quot;</span> <span class="na">title</span><span class="o">=</span><span class="s">&quot;go to this URL&quot;</span><span class="p">&gt;</span>{{ trigger.rss_url }}<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;</span> <span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{{ trigger.joplin_folder }}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{{ trigger.date_triggered  }}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{{ trigger.date_created}}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>{{ trigger.status }}<span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
                <span class="p">&lt;</span><span class="nt">td</span><span class="p">&gt;</span>
                    <span class="p">&lt;</span><span class="nt">button</span> <span class="na">type</span><span class="o">=</span><span class="s">&quot;button&quot;</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-danger&quot;</span> <span class="na">data-toggle</span><span class="o">=</span><span class="s">&quot;modal&quot;</span> <span class="na">data-target</span><span class="o">=</span><span class="s">&quot;#trigger{{ trigger.id }}&quot;</span><span class="p">&gt;</span>Delete<span class="p">&lt;/</span><span class="nt">button</span><span class="p">&gt;</span>
                    <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal fade&quot;</span> <span class="na">id</span><span class="o">=</span><span class="s">&quot;trigger{{ trigger.id }}&quot;</span> <span class="na">tabindex</span><span class="o">=</span><span class="s">&quot;-1&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;dialog&quot;</span> <span class="na">aria-labelledby</span><span class="o">=</span><span class="s">&quot;trigger{{ trigger.id}}Label&quot;</span> <span class="na">aria-hidden</span><span class="o">=</span><span class="s">&quot;true&quot;</span><span class="p">&gt;</span>
                      <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal-dialog&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;document&quot;</span><span class="p">&gt;</span>
                        <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal-content&quot;</span><span class="p">&gt;</span>
                          <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal-header&quot;</span><span class="p">&gt;</span>
                            <span class="p">&lt;</span><span class="nt">h5</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal-title&quot;</span><span class="p">&gt;</span>Deletion : {{ trigger.description }}<span class="p">&lt;/</span><span class="nt">h5</span><span class="p">&gt;</span>
                            <span class="p">&lt;</span><span class="nt">button</span> <span class="na">type</span><span class="o">=</span><span class="s">&quot;button&quot;</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;close&quot;</span> <span class="na">data-dismiss</span><span class="o">=</span><span class="s">&quot;modal&quot;</span> <span class="na">aria-label</span><span class="o">=</span><span class="s">&quot;Close&quot;</span><span class="p">&gt;</span>
                              <span class="p">&lt;</span><span class="nt">span</span> <span class="na">aria-hidden</span><span class="o">=</span><span class="s">&quot;true&quot;</span><span class="p">&gt;</span><span class="ni">&amp;times;</span><span class="p">&lt;/</span><span class="nt">span</span><span class="p">&gt;</span>
                            <span class="p">&lt;/</span><span class="nt">button</span><span class="p">&gt;</span>
                          <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
                          <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal-body&quot;</span><span class="p">&gt;</span>
                            <span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>are your sure you want to delete this trigger ? {{ trigger.description }}<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
                          <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
                          <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;modal-footer&quot;</span><span class="p">&gt;</span>
                            <span class="p">&lt;</span><span class="nt">button</span> <span class="na">type</span><span class="o">=</span><span class="s">&quot;button&quot;</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-secondary&quot;</span> <span class="na">data-dismiss</span><span class="o">=</span><span class="s">&quot;modal&quot;</span><span class="p">&gt;</span>Close<span class="p">&lt;/</span><span class="nt">button</span><span class="p">&gt;</span>
                            <span class="p">&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;{{ url_for(&#39;delete&#39;, trigger_id=trigger.id)}}&quot;</span> <span class="na">class</span><span class="o">=</span><span class="s">&quot;btn btn-danger&quot;</span> <span class="na">role</span><span class="o">=</span><span class="s">&quot;button&quot;</span><span class="p">&gt;</span>Delete it<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
                          <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
                        <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
                      <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
                    <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
                <span class="p">&lt;/</span><span class="nt">td</span><span class="p">&gt;</span>
            <span class="p">&lt;/</span><span class="nt">tr</span><span class="p">&gt;</span>
        {% endfor %}
        <span class="p">&lt;/</span><span class="nt">tbody</span><span class="p">&gt;</span>
        {% endif %}
    <span class="p">&lt;/</span><span class="nt">table</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>


{% endblock %}
</pre></div>


<h4>... un Model</h4>
<ul>
<li>Django</li>
</ul>
<div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.db</span> <span class="kn">import</span> <span class="n">models</span>


<span class="k">class</span> <span class="nc">Rss</span><span class="p">(</span><span class="n">models</span><span class="o">.</span><span class="n">Model</span><span class="p">):</span>

    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Rss</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">CharField</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mi">200</span><span class="p">,</span> <span class="n">unique</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">status</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">BooleanField</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">notebook</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">CharField</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mi">200</span><span class="p">)</span>
    <span class="n">url</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">URLField</span><span class="p">()</span>
    <span class="n">tag</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">CharField</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span> <span class="n">null</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">blank</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">date_triggered</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">DateTimeField</span><span class="p">(</span><span class="n">auto_now</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">auto_created</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="c1"># to ignore the not well formed RSS feeds</span>
    <span class="c1"># bozo detection https://pythonhosted.org/feedparser/bozo.html?highlight=bozo</span>
    <span class="c1"># default is False : we do not ignore not well formed Feeds.</span>
    <span class="n">bypass_bozo</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">BooleanField</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>

<span class="sd">        :return: string representing object</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="s2">&quot;RSS </span><span class="si">%s</span><span class="s2"> </span><span class="si">%s</span><span class="s2">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">status</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
</pre></div>


<ul>
<li>Starlette </li>
</ul>
<div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">orm</span>

<span class="k">class</span> <span class="nc">Trigger</span><span class="p">(</span><span class="n">orm</span><span class="o">.</span><span class="n">Model</span><span class="p">):</span>
    <span class="n">__tablename__</span> <span class="o">=</span> <span class="s2">&quot;trigger&quot;</span>
    <span class="n">__database__</span> <span class="o">=</span> <span class="n">database</span>
    <span class="n">__metadata__</span> <span class="o">=</span> <span class="n">metadata</span>

    <span class="nb">id</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">Integer</span><span class="p">(</span><span class="n">primary_key</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">rss_url</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">String</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mi">255</span><span class="p">)</span>
    <span class="n">joplin_folder</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">String</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mi">80</span><span class="p">)</span>
    <span class="n">description</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">String</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mi">200</span><span class="p">)</span>
    <span class="n">date_created</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">DateTime</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">)</span>
    <span class="n">date_triggered</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">DateTime</span><span class="p">(</span><span class="n">allow_null</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">status</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">Boolean</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">Text</span><span class="p">(</span><span class="n">allow_null</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">date_result</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">DateTime</span><span class="p">(</span><span class="n">allow_null</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">provider_failed</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">Integer</span><span class="p">(</span><span class="n">allow_null</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="n">consumer_failed</span> <span class="o">=</span> <span class="n">orm</span><span class="o">.</span><span class="n">Integer</span><span class="p">(</span><span class="n">allow_null</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div>


<h4>... Un Forms</h4>
<ul>
<li>Django</li>
</ul>
<p>je vous fais grâce du template du formulaire, le but étant de se focaliser sur les éléments identiques ;)</p>
<div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">RssForm</span><span class="p">(</span><span class="n">forms</span><span class="o">.</span><span class="n">ModelForm</span><span class="p">):</span>

    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        RSS Form</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="c1"># Get initial data passed from the view</span>
        <span class="nb">super</span><span class="p">(</span><span class="n">RssForm</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fields</span><span class="p">[</span><span class="s1">&#39;notebook&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">choices</span> <span class="o">=</span> <span class="n">folders</span><span class="p">()</span>

    <span class="k">class</span> <span class="nc">Meta</span><span class="p">:</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">Rss</span>
        <span class="n">exclude</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;date_triggered&#39;</span><span class="p">,)</span>
        <span class="n">widgets</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s1">&#39;name&#39;</span><span class="p">:</span> <span class="n">TextInput</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;class&#39;</span><span class="p">:</span> <span class="s1">&#39;form-control&#39;</span><span class="p">}),</span>
            <span class="s1">&#39;url&#39;</span><span class="p">:</span> <span class="n">TextInput</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;class&#39;</span><span class="p">:</span> <span class="s1">&#39;form-control&#39;</span><span class="p">}),</span>
            <span class="s1">&#39;notebook&#39;</span><span class="p">:</span> <span class="n">TextInput</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;class&#39;</span><span class="p">:</span> <span class="s1">&#39;form-control&#39;</span><span class="p">}),</span>
            <span class="s1">&#39;tag&#39;</span><span class="p">:</span> <span class="n">TextInput</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;class&#39;</span><span class="p">:</span> <span class="s1">&#39;form-control&#39;</span><span class="p">}),</span>
            <span class="s1">&#39;status&#39;</span><span class="p">:</span> <span class="n">TextInput</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;class&#39;</span><span class="p">:</span> <span class="s1">&#39;form-control&#39;</span><span class="p">}),</span>
            <span class="s1">&#39;bypass_bozo&#39;</span><span class="p">:</span> <span class="n">CheckboxInput</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;class&#39;</span><span class="p">:</span> <span class="s1">&#39;checkbox&#39;</span><span class="p">}),</span>
        <span class="p">}</span>

    <span class="n">notebook</span> <span class="o">=</span> <span class="n">forms</span><span class="o">.</span><span class="n">ChoiceField</span><span class="p">()</span>
</pre></div>


<ul>
<li>Starlette </li>
</ul>
<div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">typesystem</span>


<span class="k">class</span> <span class="nc">TriggerSchema</span><span class="p">(</span><span class="n">typesystem</span><span class="o">.</span><span class="n">Schema</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">       Schema to define the structure of a Trigger</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">rss_url</span> <span class="o">=</span> <span class="n">typesystem</span><span class="o">.</span><span class="n">String</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;RSS URL&quot;</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">255</span><span class="p">)</span>
    <span class="n">joplin_folder</span> <span class="o">=</span> <span class="n">typesystem</span><span class="o">.</span><span class="n">String</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Joplin Folder&quot;</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">80</span><span class="p">)</span>
    <span class="n">description</span> <span class="o">=</span> <span class="n">typesystem</span><span class="o">.</span><span class="n">String</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Description&quot;</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">200</span><span class="p">)</span>
    <span class="n">status</span> <span class="o">=</span> <span class="n">typesystem</span><span class="o">.</span><span class="n">Boolean</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Status&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
</pre></div>


<h4>... Un Routage</h4>
<ul>
<li>Django</li>
</ul>
<div class="highlight"><pre><span></span><span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">&#39;admin/&#39;</span><span class="p">,</span> <span class="n">admin</span><span class="o">.</span><span class="n">site</span><span class="o">.</span><span class="n">urls</span><span class="p">),</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="n">RssListView</span><span class="o">.</span><span class="n">as_view</span><span class="p">(),</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;base&#39;</span><span class="p">),</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="n">RssListView</span><span class="o">.</span><span class="n">as_view</span><span class="p">(),</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;rss&#39;</span><span class="p">),</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">&#39;add/&#39;</span><span class="p">,</span> <span class="n">RssCreateView</span><span class="o">.</span><span class="n">as_view</span><span class="p">(),</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;add&#39;</span><span class="p">),</span>
    <span class="n">url</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;^edit/(?P&lt;pk&gt;\d+)$&#39;</span><span class="p">,</span> <span class="n">RssUpdateView</span><span class="o">.</span><span class="n">as_view</span><span class="p">(),</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;edit&#39;</span><span class="p">),</span>
    <span class="p">[</span><span class="o">...</span><span class="p">]</span>
<span class="p">]</span>
</pre></div>


<ul>
<li>Starlette </li>
</ul>
<div class="highlight"><pre><span></span><span class="n">app</span> <span class="o">=</span> <span class="n">Starlette</span><span class="p">(</span>
    <span class="n">debug</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
    <span class="n">routes</span><span class="o">=</span><span class="p">[</span>
        <span class="n">Route</span><span class="p">(</span><span class="s1">&#39;/&#39;</span><span class="p">,</span> <span class="n">homepage</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;GET&#39;</span><span class="p">,</span> <span class="s1">&#39;POST&#39;</span><span class="p">],</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;homepage&#39;</span><span class="p">),</span>
        <span class="n">Route</span><span class="p">(</span><span class="s1">&#39;/id/{trigger_id:int}&#39;</span><span class="p">,</span> <span class="n">homepage</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;POST&#39;</span><span class="p">,</span> <span class="s1">&#39;GET&#39;</span><span class="p">],</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;homepage&#39;</span><span class="p">),</span>
        <span class="n">Route</span><span class="p">(</span><span class="s1">&#39;/delete/{trigger_id:int}&#39;</span><span class="p">,</span> <span class="n">delete</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;GET&#39;</span><span class="p">],</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;delete&#39;</span><span class="p">),</span>
        <span class="n">Mount</span><span class="p">(</span><span class="s1">&#39;/static&#39;</span><span class="p">,</span> <span class="n">StaticFiles</span><span class="p">(</span><span class="n">directory</span><span class="o">=</span><span class="s1">&#39;static&#39;</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s1">&#39;static&#39;</span><span class="p">)</span>
    <span class="p">],</span>
<span class="p">)</span>
</pre></div>


<p>Voilou pour l'essentiel, si vous souhaitez comparer intégralement les 2 projets, au dossier/fichier pret, vous avez les liens sur github au dessus.</p>
<p>Pour ma part je trouve starlette et ses amis, modulaires comme il faut. On dirait qu'on plug des pièces de tétris au fur et à mesure pour obtenir à la fin un projet costaud.</p>
