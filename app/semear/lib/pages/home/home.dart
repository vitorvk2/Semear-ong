import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:semear/envs.dart';
import 'package:semear/pages/home/home.service.dart';
import 'package:semear/pages/oficina_detalhes/oficina_detalhes.dart';
import 'package:semear/paletas/paleta.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<dynamic> oficinas = [];

  void getOficinasOnState() async {
    oficinas = await getOficinas();
    setState(() {});
  }

  @override
  void initState() {
    super.initState();
    getOficinasOnState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.all(30),
          child: Column(
            children: [
              Container(
                width: MediaQuery.of(context).size.width,
                margin: EdgeInsets.only(bottom: 40),
                child: Text(
                  "Suas oficinas",
                  style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
                ),
              ),
              Expanded(
                child: ListView.builder(
                  itemCount: oficinas.length,
                  itemBuilder: (c, i) {
                    return Container(
                      margin: EdgeInsets.only(bottom: 25),
                      child: Column(
                        children: [
                          oficinas[i]["imagens"].length > 0
                              ? Container(
                                  height: 200,
                                  decoration: BoxDecoration(
                                    borderRadius:
                                        BorderRadius.all(Radius.circular(14)),
                                    image: DecorationImage(
                                        image: NetworkImage(url_semear +
                                            oficinas[i]["imagens"][0]),
                                        fit: BoxFit.cover),
                                  ),
                                )
                              : Container(),
                          Container(
                            padding: EdgeInsets.all(25),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  mainAxisAlignment:
                                      MainAxisAlignment.spaceBetween,
                                  children: [
                                    Text(
                                      oficinas[i]['nome'],
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.bold,
                                        fontSize: 25,
                                      ),
                                    ),
                                    Text(
                                      oficinas[i]['horario'],
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                  ],
                                ),
                                Divider(
                                  color: Color(0x01000001),
                                ),
                                Text(
                                  "Prof." +
                                      oficinas[i]['orientador__user__nome'],
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: 17,
                                  ),
                                ),
                                Divider(
                                  color: Color(0x01000001),
                                ),
                                TextButton(
                                  onPressed: () {
                                    Navigator.of(context).push(
                                      CupertinoPageRoute(
                                        builder: (ctx2) => OficinaDetalhesPage(
                                          oficinaId: oficinas[i]['id'],
                                        ),
                                      ),
                                    );
                                  },
                                  child: Padding(
                                    padding: const EdgeInsets.all(2.0),
                                    child: Text(
                                      "Ver mais",
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
                            ),
                          ),
                        ],
                      ),
                      decoration: BoxDecoration(
                        color: Color(0xffFB8500),
                        borderRadius: BorderRadius.all(Radius.circular(14)),
                      ),
                    );
                  },
                ),
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
