import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(40.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text("Semear", style: TextStyle(fontSize: 40),),
                Divider(),
                Text("Login aluno", style: TextStyle(fontSize: 20)),
                Divider(),
                Divider(),
                Divider(),
                TextField(
                  decoration: InputDecoration(
                    hintText: "Usuário",
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(8))
                    )
                  ),
                ),
                Divider(),
                TextField(
                  obscureText: true,
                  decoration: InputDecoration(
                    hintText: "Senha",
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(8))
                    )
                  ),
                ),
                Divider(),
                TextButton(
                  onPressed: null, 
                  child: Padding(
                    padding: const EdgeInsets.all(7.0),
                    child: Text(
                      "Entrar",
                      style: TextStyle(fontSize: 18),
                    ),
                  ),
                  style: TextButton.styleFrom(
                    primary: Colors.black,
                    backgroundColor: Colors.yellow
                  ),
                )
              ],
            ),
          ),
        )
      ),
    );
  }
}