import asyncio

async def greet(name):
    await asyncio.sleep(5)
    print(f"Hello {name}!")
async def age(name):
    await asyncio.sleep(1)
    print(f"How old are you {name}?")
async def colour(name):
    await asyncio.sleep(0+.2)
    print(f"What's your favourite colour {name}?")

async def main():
    tasks = [
        asyncio.create_task(greet("Grace")),
        asyncio.create_task(colour("Grace")),
        asyncio.create_task(age("Grace"))
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())

#
# async def name():
#     print("My name is Billy W.")
#
# name()
#
# async def function():
# #     print("This is ")
# #     await asyncio.sleep(1)
# #     print('asynchronous programming')
# #     await asyncio.sleep(1)
# #     print('and not multi-threading')
# #
# # asyncio.run(function())
#
# # async def foo():
# #     print("foo starting")
# #     await asyncio.sleep(1)
# #     print("foo done")
# #
# # async def bar():
# #     print("bar starting")
# #     await asyncio.sleep(2)
# #     print("bar done")
# #
# # async def main():
# #     await asyncio.gather(foo(), bar())
#
# # asyncio.run(name())
#
#
#
