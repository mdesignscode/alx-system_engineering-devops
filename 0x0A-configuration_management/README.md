<h1>Configuration Management<h1>

<p>As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

Automation plays an essential role in server configuration management. It’s the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool’s specific language and features. Automation is, in fact, the heart of configuration management for servers, and that’s why it’s common to also refer to configuration management tools as Automation Tools or IT Automation Tools.

Another common term used to describe the automation features implemented by configuration management tools is Server Orchestration or IT Orchestration, since these tools are typically capable of managing one to hundreds of servers from a central controller machine.<p>


<h2>Puppet<h2>
<p>Puppet is an open-source software that provides tools for automating the handling of changes to a system<p>

<h3>The agent-master architecture<h3>

<p>When set up as an agent-master architecture, a Puppet master server controls the configuration information, and each managed agent node requests its own configuration catalog from the master.

In this architecture, managed nodes run the Puppet agent application, usually as a background service. One or more servers run the Puppet master application, Puppet Server.

Periodically, each Puppet agent sends facts to the Puppet master, and requests a catalog. The master compiles and returns that node’s catalog, using several sources of information it has access to.

Once it receives a catalog, Puppet agent applies it to the node by checking each resource the catalog describes. If it finds any resources that are not in their desired state, it makes the changes necessary to correct them. Or, in no-op mode, it reports on what changes would have been done.

After applying the catalog, the agent sends a report to the Puppet master.<p>
