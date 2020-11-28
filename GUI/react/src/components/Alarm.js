import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col';


class Alarm extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            id: props.data.id,
            time: props.data.id == "ID" ? "hh.mm.ss" : this.calculateDate(props.data.date)[1],
            date: props.data.id == "ID" ? "dd.mm.yyyy" : this.calculateDate(props.data.date)[0],
            affectedSystems: props.data.affectedSystems,
            suspectedAttackType: props.data.suspectedAttackType,
            probability: props.data.probability,
            automaticReaction: props.data.automaticReaction,
            checklist: props.data.checklist,
            category: this.calculateCatergory(props.data.probability)
        };
    }

    calculateCatergory(probability) {
        if (probability >= 95) { return ["critical", '#E94D4D'] }
        else if (probability >= 85) { return ["major", '#FF994F'] }
        else if (probability == 0) { return ["risk", "#909190"] }
        else { return ["minor", '#EDC535'] };
    }

    calculateDate(timestamp) {
        let now = new Date(timestamp);
        let year = now.getFullYear();
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        let month = months[now.getMonth()];
        let day = now.getDate();
        let hours = now.getHours();
        let minutes = now.getMinutes();
        let seconds = now.getSeconds();
        let time = (hours < 10 ? "0" + hours.toString() : hours.toString()) + ":" + (minutes < 10 ? "0" + minutes.toString() : minutes.toString()) + ":" + (seconds < 10 ? "0" + seconds.toString() : seconds.toString());
        let date = (day < 10 ? "0" + day.toString() : day.toString()) + "." + month + "." + year;
        return [`${date}`, `${time}`]
    }

    render() {
        return (
            <Card>

                <Card.Header>
                    <Accordion.Toggle as={Card.Header} class="p-0" eventKey={this.state.id == "ID" ? "" : this.props}>
                        <Row>
                            <h5 class="font-weight-lighter ml-2 mt-n2">Alarm #{this.state.id}</h5>
                        </Row>
                        <Row>
                            <h3 class="ml-2 mb-n1">{this.state.suspectedAttackType}</h3>
                            <div class="tag ml-2 mt-1" style={{ "background-color": this.state.category[1] }}>
                                &#8205; &#8205; {this.state.category[0]} &#8205; &#8205;
                            </div>
                            <div class="text-right w-100 mt-n4">
                                {this.state.date} {this.state.time}
                            </div>
                        </Row>
                    </Accordion.Toggle>
                </Card.Header>

                <Accordion.Collapse eventKey={this.props}>
                    <Card.Body style={{ "border-color": "red" }}>
                        <Row>
                            <Col>
                                <Row><h6 class="ml-2 mt-n2">Propability</h6></Row>
                                <Row><h2 class="ml-2 mt-n2 font-weight-lighter">{this.state.probability}%</h2></Row>
                                <Row><h6 class="ml-2">Affected Systems</h6></Row>
                                <Row><h2 class="ml-2 mt-n2 font-weight-lighter">{this.state.affectedSystems.join(', ')}</h2></Row>
                                <Row><h6 class="ml-2">Automatic Reaction</h6></Row>
                                <Row><h2 class="ml-2 mt-n2 mb-n2 font-weight-lighter">{this.state.automaticReaction.length !== 0 ? this.state.automaticReaction.join(", ") : "None"}</h2></Row>
                            </Col>
                            <Col>
                                <h6 class="mt-n2">Checklist</h6>
                                <Form.Group controlId="formBasicCheckbox" class="mb-n2">
                                    {this.state.checklist.map(check => {
                                        return <Form.Check type="checkbox" label={<h4 class="font-weight-lighter">{check}</h4>} id={check} />
                                    })}
                                </Form.Group>
                            </Col>
                        </Row>
                    </Card.Body>
                </Accordion.Collapse>
            </Card >);
    }
}

export default Alarm;
