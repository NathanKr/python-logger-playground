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


<h2>Full flexibility setup</h2>
The setup of logger_per_module allow full flexibility :
<ul>
<li>Send all modules logs to root</li>
<li>Send each module log to its log file</li>
<li>Mix of the above</li>
</ul>

And what if we want to see in root log just part of the modules log , we simply set these module log level to e.g. Warning or Error , this is easy by putting this in config.py

<h2>log utils</h2>
i have added in log_utils directory a small helper function called args_to_string which can be used to preaty print the function arguments. you can use it with logger

