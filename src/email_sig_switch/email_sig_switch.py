from email_sig_switch.zan_dmenu import select_file_or_dir
from shutil import copyfile


PROMPT = "Which signature do you want?"
SIGS_BASE_DIR = "/home/zan/sync/dat/email-signatures/"
SIGS_DIR = SIGS_BASE_DIR + "saved-signatures/"
SIG_FILE = SIGS_BASE_DIR + "signature.html"

def switch_signature():
    new_sig_file = select_file_or_dir(PROMPT, SIGS_DIR, recurse=True)
    copyfile(new_sig_file, SIG_FILE)
