"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment


class MyXBlock(XBlock):
    """
    An example XBlock from a tutorial.
    """
    upvotes = Integer(help="Number of votes", default=0,
                      scope=Scope.user_state_summary)
    downvotes = Integer(help="Number of down votes", default=0,
                        scope=Scope.user_state_summary)
    voted = Boolean(help="Has this student voted?", default=False,
                    scope=Scope.user_state)
    link_url = String(help="An external link", default='http://www.google.com',
                      scope=Scope.user_state_summary)
    link_name = String(help="Name to display for external link", default='Google Search Engine',
                       scope=Scope.user_state_summary)
    description = String(help="A description of the link",
                         default='A popular internet search engine.',
                         scope=Scope.user_state_summary)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def studio_view(self, context=None):
        """
        The studio view of the MyXBlock, allowing authors
        to configure the XBlock.
        """
        html = pkg_resources.resource_string(__name__, "static/html/myxblock_edit.html")
        link_url = self.link_url or ''
        frag = Fragment(html.format(link_url=link_url,
                                    link_name=self.link_name,
                                    description=self.description))
        js_str = pkg_resource.resource_string(__name__, "static/js/simplevideo_edit.js")
        frag.add_javascript(js_str)
        frag.initialize_js('MyXBlockEditBlock')
        
        return frag

    def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/myxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/myxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/myxblock.js"))
        frag.initialize_js('MyXBlock')
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.link_url = data.get('link_url')
        self.link_name = data.get('link_name')
        self.description = data.get('description')

        return {'result': 'success'}

    @XBlock.json_handler
    def vote(self, data, suffix=''): # pylint: disable=unused-argument
        """
        Update the vote count in response to a user action.
        """
        # Here is where we would prevent a student from voting twice, but then
        # we couldn't click more than once in the demo!
        #
        #     if self.voted:
        #         log.error("cheater!")
        #         return

        if data['voteType'] == 'up':
            self.upvotes += 1
        elif data['voteType'] == 'down':
            self.downvotes +=1
        else:
            log.error('error!')
            return
        
        self.voted = True
        return {'up': self.upvotes, 'down': self.downvotes}
        

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MyXBlock",
             """<myxblock/>
             """),
            ("Multiple MyXBlock",
             """<vertical_demo>
                <myxblock/>
                <myxblock/>
                <myxblock/>
                </vertical_demo>
             """),
        ]
