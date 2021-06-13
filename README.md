<h2>Motivation</h2>
basic python logger


<h2>common_logger</h2>
Here the root logger is defined and module utils1 and utils2 use it to write to root.log

<h2>logger_per_module</h2>
<ul>
<li>Here utils1.py and utils2.py have their own logger and they write to utils1.log and utils2.log repectively</li>
<li>because the root logger is defined in app.py it will be used also by utils1.py and utils2.py</li>
<li>utils1.py is using also console logger</li>
</ul>


