"""
    Course Subsection Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_course_subsection import IosCourseSubsection
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosCourseSubsection(IosLoginSmoke):
    """
    Course Dashboard screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Verify that Course Subsection screen will show following Header contents:
                Back icon
                Specific "<Topic name>" as Title
            Verify that user should be able to go back by clicking Back icon
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_subsection = IosCourseSubsection(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert strings.COURSE_NAME_IOS in ios_my_courses_list.load_course_details_screen().text

        assert ios_subsection.get_subsection_component_title()
        section_name = ios_subsection.get_subsection_component_title().text
        ios_subsection.get_subsection_component_title().click()
        assert ios_subsection.get_subsection_title()[0].text == section_name

        back_icon = ios_subsection.get_navigation_back_icon()[0]
        assert back_icon.get_attribute('visible') == 'true'
        back_icon.click()

    def test_subsection_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user should be able to view these on Every Topic in the list:
                Topic name
                Topic icon
            download icon to video (if available)
            Verify that on Clicking any topic Specific resource screen should be loaded successfully
        """

        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_subsection = IosCourseSubsection(set_capabilities, setup_logging)

        assert ios_course_dashboard_page.get_course_title().text in strings.COURSE_NAME_IOS
        subsection_component = ios_subsection.get_subsection_component()[0]
        subsection_component.click()
        assert ios_subsection.get_course_subsection_header_label()
        assert ios_subsection.get_subsection_html_topic_title()

        html_component = ios_subsection.get_subsection_component()[0]
        html_component.click()
        assert ios_subsection.get_subsection_title()[0].text == strings.COURSE_SUBSECTION_CONTENT_ROW_TEXT_IOS
        back_icon = ios_subsection.get_navigation_back_icon()[0]
        assert back_icon.get_attribute('visible') == 'true'
        back_icon.click()

        video_component = ios_subsection.get_subsection_component()[1]
        assert strings.COURSE_SUBSECTION_VIDEO_ROW_TEXT_IOS in video_component.text
        assert ios_subsection.get_course_item_download_icon()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course subsection screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)

        ios_course_dashboard_page.navigate_to_main_dashboard(set_capabilities)
        ios_main_dashboard_page.get_drawer_icon().click()
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info(' Ending Test Case --')
