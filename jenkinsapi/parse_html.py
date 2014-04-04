from HTMLParser import HTMLParser

class JenkinsHTMLParser(HTMLParser):
    """
    This class helps parse the result html from triggering Jenkins job
    Parsed value looks like as below:
    <script defer="true">updateBuildHistory("/job/Ready/buildHistory/ajax",\
        4809);</script>
    We will extract the job id from this tag in the response html
    """
    
    def __init__(self):
        HTMLParser.__init__(self)
        #updateBuildHistory("/job/Ready/buildHistory/ajax",4809);
        self.jobid_elt = None
        self.attr_found = False 
    
    def handle_starttag(self, tag, attrs):
        if tag =='script':
            for name, value in attrs:
                if name == 'defer' and value == 'true':
                    self.attr_found = True
                    break
    
    def handle_data(self, data):
        if self.attr_found:
            self.jobid_elt  = data

        self.attr_found = False

    def get_job_id(self):
        id = int(''.join([i for i in self.jobid_elt if i.isdigit()]))
        return id
