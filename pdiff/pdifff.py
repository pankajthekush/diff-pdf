import subprocess, logging,tempfile,sys, time, pathlib
from s3 import upload_file

# logging
formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(process)d %(levelname)-8s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
# end logging


# change this if you want your custom caching 
# I am using s3 for caching with life cycle
def cache_file(file_path):
    public_s3, private_s3 = upload_file(fname=file_path,acl='publi-read')
    return {'public':public_s3,'private':private_s3}


def diff_pdf(f1,f2,**kwargs):
    do_cache = kwargs.get('do_cache',None) 
    
    out_dict = dict()
    with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',suffix='.pdf') as f:
        out_proc = subprocess.run(['xvfb-run','-a','diff-pdf','--skip-identical', '--grayscale', '--output-diff',f.name,f1,f2])
        return_code= out_proc.returncode
        out_dict['return_code'] = return_code
        out_dict['diff_file'] = f.name
        if do_cache and return_code == 1: # 1 means there is  diff else not
            cache_data = cache_file(f.name)
            out_dict['cached_data'] = cache_data
        else:
            out_dict['cached_data'] = None

    return out_dict