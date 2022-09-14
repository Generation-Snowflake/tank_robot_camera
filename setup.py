from setuptools import setup

package_name = 'cam_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cstick',
    maintainer_email='p.ektanat@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cam_s = cam_sub.cam_sub_node:main',
            'cam_p = cam_sub.cam_pub_node:main'
        ],
    },
)
