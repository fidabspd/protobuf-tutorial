import addressbook_pb2
from google.protobuf import text_format


PBTXT_FILEPATH = "./addressbook.pbtxt"
SERIALIZED_FILEPATH = "ADDRESS_BOOK_FILE"


def parse_adressbook_pbtxt(pbtxt_filepath: str):
    address_book = addressbook_pb2.AddressBook()

    with open(pbtxt_filepath, "r", encoding="UTF-8") as f:
        text_format.Parse(f.read(), address_book)

    return address_book


# Load the address book from pbtxt file.
address_book_from_pbtxt_file = parse_adressbook_pbtxt(PBTXT_FILEPATH)
print("### address book (from pbtxt file):\n{}".format(address_book_from_pbtxt_file))

# # Write the address book back to disk as serialized file.
# with open(SERIALIZED_FILEPATH, "wb") as f:
#     f.write(address_book_from_pbtxt_file.SerializeToString())

# # Read the existing address book.
# address_book_from_serialized_file = addressbook_pb2.AddressBook()
# with open(SERIALIZED_FILEPATH, "rb") as f:
#     address_book_from_serialized_file.ParseFromString(f.read())
# print("### address book (from serialized file):\n{}".format(address_book_from_serialized_file))
