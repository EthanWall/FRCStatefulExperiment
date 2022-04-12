import globe
from loops.loop import Loop


def run_drive():
    fwd = globe.stick.forward
    rot = globe.stick.rotation

    globe.drivetrain.arcade_drive(fwd, rot)


class TeleOpLoop(Loop):

    def on_start(self, timestamp):
        globe.drivetrain.zero_sensors()

    def on_update(self, timestamp):
        run_drive()

    def on_end(self, timestamp):
        globe.drivetrain.stop()
