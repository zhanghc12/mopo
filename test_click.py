# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:12:06 2020

@author: huangl
"""
import sys
import click


# @click.command()
# @click.argument('filename')
# def touch(filename):
#    click.echo(filename)
#
# if __name__ == '__main__':
#    sys.argv = ['temp5.py', 'foo.txt']
#    touch()



@click.command(
    name='run_local',
    context_settings={'ignore_unknown_options': True})
@click.argument('src', nargs=-1)  # -1是不定长度
@click.argument('dst', nargs=1)
def copy(src, dst):
    for fn in src:
        click.echo('move %s to folder %s' % (fn, dst))


@click.command(
    name='run_local',
    context_settings={'ignore_unknown_options': True})
@click.argument('src', nargs=-1)  # -1是不定长度
@click.argument('dst', nargs=1)
def copy(src, dst):
    for fn in src:
        click.echo('move %s to1 folder %s' % (fn, dst))


if __name__ == '__main__':
    sys.argv = ['temp5.py', 'foo1.txt', "foo2.txt", "foo2.txt", "fold"]
    copy()