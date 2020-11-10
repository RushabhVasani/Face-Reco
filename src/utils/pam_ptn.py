from os import chdir, getcwd

from execnet import makegateway

def call_python_version(Version, Module, Function, ArgumentList):
    gw      = makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return  channel.receive()


def pam_sm_authenticate(pamh, flags, args):

    cur = getcwd()
    print "facerec running.."

    try:
        chdir("/usr/lib/Auth/Facerec/")
        if call_python_version("3", "compare", "authenticate", []):
            chdir(cur)
            return pamh.PAM_SUCCESS
        else:
            chdir(cur)
            print("facerec did not recognize you! Please enter the password!")
            return pamh.PAM_SYSTEM_ERR

    except Exception as e:
        print("An unexpected error occoured... Please enter the password!")


def pam_sm_open_session(pamh, flags, args):

    cur = getcwd()
    print "facerec running.."

    try:
        chdir("/usr/lib/Auth/Facerec/")
        if call_python_version("3", "compare", "authenticate", []):
            chdir(cur)
            return pamh.PAM_SUCCESS
        else:
            chdir(cur)
            print("facerec did not recognize you! Please enter the password!")
            return pamh.PAM_SYSTEM_ERR

    except Exception as e:
        print("An unexpected error occoured... Please enter the password!")

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS
