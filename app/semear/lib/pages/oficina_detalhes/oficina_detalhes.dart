import 'package:flutter/material.dart';
import 'package:semear/paletas/paleta.dart';

class OficinaDetalhesPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.all(30),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                width: MediaQuery.of(context).size.width,
                margin: EdgeInsets.only(bottom: 40),
                child: Text(
                  "Título",
                  style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
                ),
              ),
              Container(
                child: Text(
                  "Oficina: ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Divider(
                color: Color(0x01000001),
              ),
              Container(
                child: Text(
                  "Horário: ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Divider(
                color: Color(0x01000001),
              ),
              Container(
                child: Text(
                  "Link: ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Divider(
                color: Color(0x01000001),
              ),
              Container(
                child: Text(
                  "Local: ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Divider(
                color: Color(0x01000001),
              ),
              Row(
                children: [
                  Container(
                    child: Text(
                      "Faltas: ",
                      style: TextStyle(fontSize: 20),
                    ),
                  ),
                  TextButton(
                    onPressed: () {}, 
                    child: Padding(
                      padding: const EdgeInsets.all(2.0),
                      child: Text(
                        "Ver",
                        style: TextStyle(
                          fontSize: 14,
                          color: Colors.black,
                        ),
                      ),
                    ),
                    style: TextButton.styleFrom(
                      backgroundColor: SemearColor[400],
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: SemearColor[400],
        items: [
          BottomNavigationBarItem(label: "pesquisar", icon: Icon(null)),
          BottomNavigationBarItem(label: "a", icon: Icon(null)),
          BottomNavigationBarItem(label: "a", icon: Icon(null)),
        ],
      ),
    );
  }
}