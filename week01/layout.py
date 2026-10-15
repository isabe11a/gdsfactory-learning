import gdsfactory as gf

gf.gpdk.PDK.activate()
top = gf.Component("week01_straights")

for y, width in [(0.0, 0.5), (10.0, 0.8)]:
    waveguide = gf.components.straight(
        length=100.0,
        width=width,
        cross_section="strip",
    )
    instance = top.add_ref(waveguide)
    instance.movey(y)

top.write_gds("week01.gds")
