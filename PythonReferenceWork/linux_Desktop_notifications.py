# https://www.youtube.com/watch?v=jHdt3WrQbr8&list=PLEtC2iwVrNRZdd5HqafuFMWjG-V_i16rO&index=7

from gi.repository import Notify
import gi
gi.require_version('Notify', '0.7')

Notify.init("Test Notifier")

notification = Notify.Notification.new("Hello\n My friend",
                                       "How are you?", "emblem-OK",)

notification.set_urgency(2)

notification.show()

# if you are making this in a virtual environment create your venv and then
# pip install pgi....then replace reference from gi to pgi in code.
