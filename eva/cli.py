import click
import os
import terminaltables


@click.command()
def eva():
    list_header = 'List of Environment Variables from .env file'
    try:
        table_data = []

        for i in open('{0}/.env'.format(os.getcwd())).readlines():
            row_list = i.strip().split('=',1)
            row_list.append(os.environ.get(row_list[0]))
            table_data.append(row_list)
    except IOError:
        click.echo('Eva could not find a .env file in the current directory.')
        exit()
    click.echo(click.style(list_header, fg='green'))
    table_data.insert(0,['Key','Value','Environment Value'])
    click.echo(terminaltables.AsciiTable(table_data).table)


if __name__ == '__main__':
    eva()