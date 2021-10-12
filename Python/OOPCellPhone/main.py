from cell_phone import CellPhone

bobs_phone = CellPhone("iPhone")

bobs_phone.receive_text("Frank: Hi Bob.")
bobs_phone.receive_text("Olivia: Thanks Bob.")

print(bobs_phone.messages)

bobs_phone.send_text()

bobs_phone.toggle_vibrate()

bobs_phone.add_contact()

print(bobs_phone.contacts)
