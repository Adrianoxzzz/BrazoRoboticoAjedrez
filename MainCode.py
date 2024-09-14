import time
import serial
import chess
import chess.engine

#Serial Comunication Initialization
esp = serial.Serial("COM4",115200)
time.sleep(2)
for i in range (7):
        esp.readline().decode("utf-8")

#ChessBoard and Engine Initialization
board = chess.Board();
print(board);
print("\n")
engine= chess.engine.SimpleEngine.popen_uci(r"C:\stockfish-windows-x86-64-sse41-popcnt\stockfish\stockfish-windows-x86-64-sse41-popcnt")
limit = chess.engine.Limit(time = 2.0)

#Game
while not board.is_game_over():
    jugada = input()    #Player Turn
    board.push_san(jugada)
    print(board)
    print("\n")
    EngineMove = engine.play(board,limit)
    board.push(EngineMove.move) #Engine Move
    print(board)
    print("\n")
    actualFEN = board.fen(); #Get Game FEN
    print(actualFEN)
    esp.write(actualFEN.encode().strip())   #Send FEN Via Serial Port
    time.sleep(1)
    print("Fen Enviado")
    response = esp.readline().decode('utf-8')
    print(response)
    if(response.strip() != actualFEN.strip()):
          print("FEN correctly recived")
          print("\n")
    else:
          print("Error reciving FEN")
engine.quit()