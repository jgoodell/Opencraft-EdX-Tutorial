"""An XBlock that will allow you to embed SoundCloud players into a XBlock."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment


class SoundCloudXBlock(XBlock):
    """
    The SoundCloud XBlock.
    """

    # <iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/299920725&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    src = String(help="The source of the track", default=None, scope=Scope.content)
    maxwidth = String(help="Maximum width of track player.", default='100%', scope=Scope.content)
    maxheight = Integer(help="Maximum height of the track player.", default=450, scope=Scope.content)
    scrolling = String(help="Whether the player scrolls the track or not.", default='no', scope=Scope.content)
    frameborder = String(help="Whether the player has a frame border or not.", default='no', scope=Scope.content)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the SoundCloudXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/soundcloud.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/soundcloud.css"))
        frag.add_javascript(self.resource_string("static/js/src/soundcloud.js"))
        frag.initialize_js('SoundCloudXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("SoundCloudXBlock",
             """
             <vertical_demo>
                 <soundcloud src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/282126708&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true" maxwidth="100%" maxheight="120" scroll="no" frameborder="no"/>
             </vertical_demo>
             """),
            ("Multiple SoundCloudXBlock",
             """<vertical_demo>
                <soundcloud/>
                <soundcloud/>
                <soundcloud/>
                </vertical_demo>
             """),
        ]
