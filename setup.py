import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="exam_course_tab_app",
    version="0.1.0",
    packages=find_packages(),
    package_data={"": ["*.html"]},  # include any Mako templates found in this repo.
    include_package_data=True,
    license="Proprietary",
    description="Adds a sparking winter wonderland to normal Open edX environments",
    long_description="",
    author="Ali Assad",
    author_email="aliassad2@hotmail.com",
    url="https://github.com/aliassad/openEdx-custom-course-tab",
    zip_safe=False,
    keywords="Django edx",
    entry_points={
        # IMPORTANT: ensure that this entry_points coincides with that of edx-platform
        #            and also that you are not introducing any name collisions.
        # https://github.com/edx/edx-platform/blob/master/setup.py#L88
        "lms.djangoapp": [
            "exam_course_tab_app = exam_course_tab_app.apps:ExamCourseTabAppConfig",
        ],
    },
    install_requires=[
        'Django',
    ],
)