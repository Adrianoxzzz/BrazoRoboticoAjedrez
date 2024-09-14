import time
import serial
import chess
import chess.engine

esp = serial.Serial("COM4",115200)
time.sleep(2)
for i in range (7):
        esp.readline().decode("utf-8")
board = chess.Board();
print(board);
print("\n")
engine= chess.engine.SimpleEngine.popen_uci(r"C:\stockfish-windows-x86-64-sse41-popcnt\stockfish\stockfish-windows-x86-64-sse41-popcnt")
limit = chess.engine.Limit(time = 2.0)
while not board.is_game_over():
    jugada = input()
    board.push_san(jugada)
    print(board)
    print("\n")
    EngineMove = engine.play(board,limit)
    board.push(EngineMove.move)
    print(board)
    print("\n")
    actualFEN = board.fen();
    print(actualFEN)
    print("\n")
    esp.write(actualFEN.encode().strip())
    time.sleep(1)
    print("Fen Enviado")
    print("\n")
    response = esp.readline().decode('utf-8')
    print(response)
    print('\n')
engine.quit()