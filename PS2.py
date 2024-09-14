import serial, time, PS
import ChessDefs,chess,chess.engine
#Inicializar Puerto Serial Con ESP32

esp = PS.InitializeSerialPort(115200)
PS.CleanBuffer(esp)

#Inicializar Tablero y Engine
board = ChessDefs.SetBoard()
engine = ChessDefs.EngineInitialize()
limit = ChessDefs.EngineTimeLimit(2.0)

while not board.is_game_over():
    ChessDefs.PlayerTurn(board)
    ChessDefs.EngineTurn(engine,limit,board)
    actualFEN = ChessDefs.GenerateFen(board)
    #PS.SendFenSerialPort(actualFEN,esp)
    #response = PS.ReadSerialPort(esp)
