'''
The main script
'''

import click
from ClusterClass import ClusterSummary
from Messages import Messages

@click.command()
@click.option('--input', '-i', help = 'Output from --uc from vsearch clustering algorithm')
def vs_locus(input):
    msg = Messages()
    #msg.info("Welcome to vs_locus (version {})".format(vs.__version__))
    msg.info("Welcome to vs_locus!")
    cluster_summary = ClusterSummary()
    cluster_summary.load_table(input)
    pass
