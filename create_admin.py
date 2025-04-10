#!/usr/bin/env python

import uuid
import click

from database.services.users import user_service_db

@click.command()
@click.argument('email')
@click.argument('password')
def create_admin(email, password):
    res = user_service_db.register_user(uuid.uuid4(), "admin", "2011-11-11", "", "", email, "" , password, True, True,
                                  True, 0, True, 0)

    if res == 0:
        click.echo(f"Пользователь {email} с ролью администратор успешно создан!")
    else:
        click.echo("Ошибка при создании пользователя")

if __name__ == '__main__':
    create_admin()
