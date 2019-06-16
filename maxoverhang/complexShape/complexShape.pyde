background(204)
size(100,100, P2D)
alien = createShape(GROUP)
head = createShape(ELLIPSE, -25, 0, 50, 50)
head.setFill(color(255))
body = createShape(RECT, -25, 45, 50, 40)
body.setFill(color(0))
# Add the two "child" shapes to the parent group
alien.addChild(body)
alien.addChild(head)
translate(50,15)


shape(alien)
