import os
import logging.config

from homework_13 import log_event


def test_success():
    log_event("Alex", "success")

    with open("login_system.log", "r") as file:
        content = file.read()

    lines = content.splitlines()

    assert "Login event - Username: Alex, Status: success" in lines[-1]
    assert "INFO" in lines[-1]


def test_expired():
    log_event("John", "expired")

    with open("login_system.log", "r") as file:
        content = file.read()

    lines = content.splitlines()

    assert "Login event - Username: John, Status: expired" in lines[-1]
    assert "WARNING" in lines[-1]


def test_failed():
    log_event("Gio", "failed")

    with open("login_system.log", "r") as file:
        content = file.read()

    lines = content.splitlines()

    assert "Login event - Username: Gio, Status: failed" in lines[-1]
    assert "ERROR" in lines[-1]