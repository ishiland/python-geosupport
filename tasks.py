from invoke import task, run

nosetests = 'nosetests --with-coverage --cover-package=geosupport --cover-html --cover-branches --cover-erase'

@task()
def test(test_type):
    if test_type == 'unit':
        cmd = ' '.join([nosetests, 'tests/unit/*'])
        run('sh -c "%s"' % cmd)
    elif test_type == 'functional':
        cmd = ' '.join([nosetests, 'tests/functional/*'])
        run('sh -c "%s"' % cmd)
    elif test_type == 'all':
        cmd = ' '.join([nosetests, 'tests/*'])
        run('sh -c "%s"' % cmd)
    else:
        print("Unknown test suite '%s'. Choose one of: unit, functional, all." % test_type)

@task
def pylint():
    run('sh -c "pylint geosupport"')
