import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:semear/pages/login/login.dart';
import 'package:semear/paletas/paleta.dart';
import 'package:shared_preferences/shared_preferences.dart';

class BottomMenuComponent extends StatelessWidget {
  final colorLetters = Colors.black54;

  void openSearch(BuildContext context) {
    print("a");
  }

  void exitApp(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext ctx) {
        return AlertDialog(
          title: Text("Deseja realmente sair?"),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Padding(
                padding: const EdgeInsets.all(2.0),
                child: Text(
                  "Cancelar",
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
            TextButton(
              onPressed: () async {
                SharedPreferences prefs = await SharedPreferences.getInstance();
                prefs.clear();

                Navigator.of(context).pushAndRemoveUntil(
                  CupertinoPageRoute(
                      builder: (BuildContext ctx) => LoginPage()),
                  (route) => false,
                );
              },
              child: Padding(
                padding: const EdgeInsets.all(2.0),
                child: Text(
                  "Sair",
                  style: TextStyle(
                    fontSize: 14,
                    color: Colors.white,
                  ),
                ),
              ),
              style: TextButton.styleFrom(
                backgroundColor: Color(0xff020129),
              ),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    List<Function> funs = [this.openSearch, this.exitApp];

    return BottomNavigationBar(
      unselectedItemColor: Colors.black54,
      fixedColor: Colors.black54,
      backgroundColor: SemearColor[400],
      onTap: (index) {
        funs[index](context);
      },
      items: [
        BottomNavigationBarItem(label: "Pesquisar", icon: Icon(Icons.search)),
        BottomNavigationBarItem(label: "Sair", icon: Icon(Icons.exit_to_app)),
      ],
    );
  }
}
