import 'package:flutter/material.dart';
import 'package:semear/envs.dart';
import 'package:semear/pages/oficina_detalhes/oficina_detalhes.service.dart';
import 'package:semear/paletas/paleta.dart';

class OficinaDetalhesPage extends StatefulWidget {
  final int oficinaId;

  OficinaDetalhesPage({required this.oficinaId});

  @override
  _OficinaDetalhesPageState createState() => _OficinaDetalhesPageState();
}

class _OficinaDetalhesPageState extends State<OficinaDetalhesPage> {
  Map<String, dynamic> detalhes = Map<String, dynamic>();

  void getDetalhes() async {
    detalhes = await detalhesOficina(widget.oficinaId);

    setState(() {});
  }

  @override
  void initState() {
    super.initState();

    getDetalhes();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.all(30),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  width: MediaQuery.of(context).size.width,
                  margin: EdgeInsets.only(bottom: 40),
                  child: Row(
                    children: [
                      IconButton(
                        padding: EdgeInsets.zero,
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                        icon: Icon(
                          Icons.arrow_back_outlined,
                          color: Colors.black,
                          size: 35,
                        ),
                        alignment: Alignment.centerLeft,
                        color: Colors.blue,
                      ),
                      Text(
                        detalhes['nome'] ?? '',
                        style: TextStyle(
                          fontSize: 30,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                Container(
                  child: Text(
                    "Oficina: " + (detalhes['nome'] ?? ''),
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                Container(
                  child: Text(
                    "Horário: " + (detalhes['horario'] ?? '---'),
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                Container(
                  child: Text(
                    "Link: " + (detalhes['link'] ?? '---'),
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                Container(
                  child: Text(
                    "Local: " + (detalhes['local'] ?? '---'),
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
                Divider(color: Color(0x01000001)),
                GridView.builder(
                  shrinkWrap: true,
                  primary: true,
                  physics: NeverScrollableScrollPhysics(),
                  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    crossAxisSpacing: 5,
                    mainAxisSpacing: 5,
                  ),
                  itemBuilder: (BuildContext ctx, int index) {
                    return Container(
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.all(Radius.circular(9)),
                        image: DecorationImage(
                          image: NetworkImage(
                            url_semear + detalhes['imagens'][index],
                          ),
                          fit: BoxFit.cover,
                        ),
                      ),
                    );
                  },
                  itemCount: detalhes['imagens'].length ?? 0,
                ),
              ],
            ),
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
